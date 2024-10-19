## Low-Temperature PEM Electrolyzer Model
"""
Python model of H2 PEM low-temp electrolyzer.

Quick Hydrogen Physics:

1 kg H2 <-> 11.1 N-m3 <-> 33.3 kWh (LHV) <-> 39.4 kWh (HHV)

High mass energy density (1 kg H2= 3,77 l gasoline)
Low volumetric density (1 Nm³ H2= 0,34 l gasoline

Hydrogen production from water electrolysis (~5 kWh/Nm³ H2)

Power:1 MW electrolyser <-> 200 Nm³/h  H2 <-> ±18 kg/h H2
Energy:+/-55 kWh of electricity --> 1 kg H2 <-> 11.1 Nm³ <-> ±10 liters
demineralized water

Power production from a hydrogen PEM fuel cell from hydrogen (+/-50%
efficiency):
Energy: 1 kg H2 --> 16 kWh
"""
# Updated as of 10/31/2022
import math
import numpy as np
import sys
import pandas as pd
from matplotlib import pyplot as plt
import scipy
from scipy.optimize import fsolve

np.set_printoptions(threshold=sys.maxsize)

def calc_current(P_T,p1,p2,p3,p4,p5,p6): #calculates i-v curve coefficients given the stack power and stack temp
    pwr,tempc=P_T
    i_stack=p1*(pwr**2) + p2*(tempc**2)+ (p3*pwr*tempc) +  (p4*pwr) + (p5*tempc) + (p6)
    return i_stack 

class PEM_electrolyzer_LT:
    """
    Create an instance of a low-temperature PEM Electrolyzer System. Each
    stack in the electrolyzer system in this model is rated at 1 MW_DC.

    Parameters
    _____________
    np_array P_input_external_kW
        1-D array of time-series external power supply

    string voltage_type
        Nature of voltage supplied to electrolyzer from the external power
        supply ['variable' or 'constant]

    float power_supply_rating_MW
        Rated power of external power supply

    Returns
    _____________

    """

    def __init__(self, input_dict, output_dict):
        self.input_dict = input_dict
        self.output_dict = output_dict

        # array of input power signal
        self.input_dict['P_input_external_kW'] = input_dict['P_input_external_kW']
        self.electrolyzer_system_size_MW = input_dict['electrolyzer_system_size_MW']

        # self.input_dict['voltage_type'] = 'variable'  # not yet implemented
        self.input_dict['voltage_type'] = 'constant'
        self.stack_input_voltage_DC = 250

        # Assumptions:
        self.min_V_cell = 1.62  # Only used in variable voltage scenario
        self.p_s_h2_bar = 31  # H2 outlet pressure
        self.stack_input_current_lower_bound = 400 #[A] any current below this amount (10% rated) will saturate the H2 production to zero, used to be 500 (12.5% of rated)
        self.stack_rating_kW = 1000  # 1 MW
        self.cell_active_area = 1250 #[cm^2]
        self.N_cells = 130
        self.max_cell_current=2*self.cell_active_area #PEM electrolyzers have a max current density of approx 2 A/cm^2 so max current is 2*cell_area

        # Constants:
        self.moles_per_g_h2 = 0.49606 #[1/weight_h2]
        self.V_TN = 1.48  # Thermo-neutral Voltage (Volts) in standard conditions
        self.F = 96485.34  # Faraday's Constant (C/mol) or [As/mol]
        self.R = 8.314  # Ideal Gas Constant (J/mol/K)

        #Additional Constants
        self.T_C = 80 #stack temperature in [C]
        self.mmHg_2_Pa = 133.322 #convert between mmHg to Pa
        self.patmo = 101325 #atmospheric pressure [Pa]
        self.mmHg_2_atm = self.mmHg_2_Pa/self.patmo #convert from mmHg to atm

        
        self.curve_coeff=self.iv_curve() #this initializes the I-V curve to calculate current
        self.external_power_supply() 

    def external_power_supply(self):
        """
        External power source (grid or REG) which will need to be stepped
        down and converted to DC power for the electrolyzer.

        Please note, for a wind farm as the electrolyzer's power source,
        the model assumes variable power supplied to the stack at fixed
        voltage (fixed voltage, variable power and current)

        TODO: extend model to accept variable voltage, current, and power
        This will replicate direct DC-coupled PV system operating at MPP
        """
        power_converter_efficiency = 1.0 # this used to be 0.95 but feel free to change as you'd like
        if self.input_dict['voltage_type'] == 'constant':

            self.input_dict['P_input_external_kW'] = \
                np.where(self.input_dict['P_input_external_kW'] >
                         (self.electrolyzer_system_size_MW * 1000),
                         (self.electrolyzer_system_size_MW * 1000),
                         self.input_dict['P_input_external_kW'])

            self.output_dict['curtailed_P_kW'] = \
                np.where(self.input_dict['P_input_external_kW'] >
                         (self.electrolyzer_system_size_MW * 1000),
                         (self.input_dict['P_input_external_kW'] -
                          (self.electrolyzer_system_size_MW * 1000)), 0)
            
            #Current used to be calculated as Power/Voltage but now it uses the IV curve
            # self.output_dict['current_input_external_Amps'] = \
            #     (self.input_dict['P_input_external_kW'] * 1000 *
            #      power_converter_efficiency) / (self.stack_input_voltage_DC *
            #                                     self.system_design())

            self.output_dict['current_input_external_Amps'] = \
                calc_current((((self.input_dict['P_input_external_kW'] *
                 power_converter_efficiency)/self.system_design()),self.T_C), *self.curve_coeff)

            self.output_dict['stack_current_density_A_cm2'] = \
                self.output_dict['current_input_external_Amps'] / self.cell_active_area

            self.output_dict['current_input_external_Amps'] = \
                np.where(self.output_dict['current_input_external_Amps'] <
                         self.stack_input_current_lower_bound, 0,
                         self.output_dict['current_input_external_Amps'])

        else:
            pass  # TODO: extend model to variable voltage and current source
    def iv_curve(self):
        """
        This is a new function that creates the I-V curve to calculate current based
        on input power and electrolyzer temperature

        current range is 0: max_cell_current+10 -> PEM have current density approx = 2 A/cm^2

        temperature range is 40 degC : rated_temp+5 -> temperatures for PEM are usually within 60-80degC

        calls cell_design() which calculates the cell voltage
        """
        current_range = np.arange(0,self.max_cell_current+10,10) 
        temp_range = np.arange(40,self.T_C+5,5)
        idx = 0
        powers = np.zeros(len(current_range)*len(temp_range))
        currents = np.zeros(len(current_range)*len(temp_range))
        temps_C = np.zeros(len(current_range)*len(temp_range))
        for i in range(len(current_range)):
            
            for t in range(len(temp_range)):
                powers[idx] = current_range[i]*self.cell_design(temp_range[t],current_range[i])*self.N_cells*(1e-3) #stack power
                currents[idx] = current_range[i]
                temps_C[idx] = temp_range[t]
                idx = idx+1
                
        curve_coeff, curve_cov = scipy.optimize.curve_fit(calc_current, (powers,temps_C), currents, p0=(1.0,1.0,1.0,1.0,1.0,1.0)) #updates IV curve coeff
        return curve_coeff
    def system_design(self):
        """
        For now, system design is solely a function of max. external power
        supply; i.e., a rated power supply of 50 MW means that the electrolyzer
        system developed by this model is also rated at 50 MW

        TODO: Extend model to include this capability.
        Assume that a PEM electrolyzer behaves as a purely resistive load
        in a circuit, and design the configuration of the entire electrolyzer
        system - which may consist of multiple stacks connected together in
        series, parallel, or a combination of both.
        """
        h2_production_multiplier = (self.electrolyzer_system_size_MW * 1000) / \
                                   self.stack_rating_kW
        self.output_dict['electrolyzer_system_size_MW'] = self.electrolyzer_system_size_MW
        return h2_production_multiplier

    def cell_design(self, Stack_T, Stack_Current):
        """

        Please note that this method is currently not used in the model. It
        will be used once the electrolyzer model is expanded to variable
        voltage supply as well as implementation of the self.system_design()
        method

        Motivation:

        The most common representation of the electrolyzer performance is the
        polarization curve that represents the relation between the current density
        and the voltage (V):
        Source: https://www.sciencedirect.com/science/article/pii/S0959652620312312

        V = N_c(E_cell + V_Act,c + V_Act,a + iR_cell)

        where N_c is the number of electrolyzer cells,E_cell is the open circuit
        voltage VAct,and V_Act,c are the anode and cathode activation over-potentials,
        i is the current density and iRcell is the electrolyzer cell resistance
        (ohmic losses).

        Use this to make a V vs. A (Amperes/cm2) graph which starts at 1.23V because
        thermodynamic reaction of water formation/splitting dictates that standard
        electrode potential has a ∆G of 237 kJ/mol (where: ∆H = ∆G + T∆S)

        10/31/2022
        ESG: https://www.sciencedirect.com/science/article/pii/S0360319906000693
        -> calculates cell voltage to make IV curve (called by iv_curve)
        Another good source for the equations used in this function: 
        https://www.sciencedirect.com/science/article/pii/S0360319918309017

        """

        # Cell level inputs:

        E_rev0 = 1.229  # (in Volts) Reversible potential at 25degC - Nerst Equation (see Note below)
        #E_th = 1.48  # (in Volts) Thermoneutral potential at 25degC - No longer used

        T_K=Stack_T+ 273.15  # in Kelvins
        # E_cell == Open Circuit Voltage - used to be a static variable, now calculated
        # NOTE: E_rev is unused right now, E_rev0 is the general nerst equation for operating at 25 deg C at atmospheric pressure
        # (whereas we will be operating at higher temps). From the literature above, it appears that E_rev0 is more correct
        # https://www.sciencedirect.com/science/article/pii/S0360319911021380 
        E_rev = 1.5184 - (1.5421 * (10 ** (-3)) * T_K) + \
                 (9.523 * (10 ** (-5)) * T_K * math.log(T_K)) + \
                 (9.84 * (10 ** (-8)) * (T_K ** 2))
        
        # Calculate partial pressure of H2 at the cathode: 
        # Uses Antoine formula (see link below)
        # p_h2o_sat calculation taken from compression efficiency calculation
        # https://www.omnicalculator.com/chemistry/vapour-pressure-of-water#antoine-equation
        A = 8.07131
        B = 1730.63
        C = 233.426
        
        p_h2o_sat_mmHg = 10 ** (A - (B / (C + Stack_T)))  #vapor pressure of water in [mmHg] using Antoine formula
        p_h20_sat_atm=p_h2o_sat_mmHg*self.mmHg_2_atm #convert mmHg to atm

        # could also use Arden-Buck equation (see below). Arden Buck and Antoine equations give barely different pressures 
        # for the temperatures we're looking, however, the differences between the two become more substantial at higher temps
    
        # p_h20_sat_pa=((0.61121*math.exp((18.678-(Stack_T/234.5))*(Stack_T/(257.14+Stack_T))))*1e+3) #ARDEN BUCK
        # p_h20_sat_atm=p_h20_sat_pa/self.patmo

        # Cell reversible voltage kind of explain in Equations (12)-(15) of below source
        # https://www.sciencedirect.com/science/article/pii/S0360319906000693
        # OR see equation (8) in the source below
        # https://www.sciencedirect.com/science/article/pii/S0360319917309278?via%3Dihub
        E_cell=E_rev0 + ((self.R*T_K)/(2*self.F))*(np.log((1-p_h20_sat_atm)*math.sqrt(1-p_h20_sat_atm))) #1 value is atmoshperic pressure in atm
        i = Stack_Current/self.cell_active_area #i is cell current density

        # Following coefficient values obtained from Yigit and Selamet (2016) -
        # https://www.sciencedirect.com/science/article/pii/S0360319916318341?via%3Dihub
        a_a = 2  # Anode charge transfer coefficient
        a_c = 0.5  # Cathode charge transfer coefficient
        i_o_a = 2 * (10 ** (-7)) #anode exchange current density
        i_o_c = 2 * (10 ** (-3)) #cathode exchange current density

        #below is the activation energy for anode and cathode - see  https://www.sciencedirect.com/science/article/pii/S0360319911021380 
        V_act = (((self.R * T_K) / (a_a * self.F)) * np.arcsinh(i / (2 * i_o_a))) + (
                ((self.R * T_K) / (a_c * self.F)) * np.arcsinh(i / (2 * i_o_c)))
        
        # equation 13 and 12 for lambda_water_content and sigma: from https://www.sciencedirect.com/science/article/pii/S0360319917309278?via%3Dihub         
        lambda_water_content = ((-2.89556 + (0.016 * T_K)) + 1.625) / 0.1875
        delta = 0.018 # [cm] reasonable membrane thickness of 180-µm NOTE: this will likely decrease in the future 
        sigma = ((0.005139 * lambda_water_content) - 0.00326) * math.exp(
            1268 * ((1 / 303) - (1 / T_K)))   # membrane proton conductivity [S/cm]
        
        R_cell = (delta / sigma) #ionic resistance [ohms]
        R_elec=3.5*(10 ** (-5)) # [ohms] from Table 1 in  https://journals.utm.my/jurnalteknologi/article/view/5213/3557
        V_cell = E_cell + V_act + (i *( R_cell + R_elec)) #cell voltage [V]
        # NOTE: R_elec is to account for the electronic resistance measured between stack terminals in open-circuit conditions
        # Supposedly, removing it shouldn't lead to large errors 
        # calculation for it: http://www.electrochemsci.org/papers/vol7/7043314.pdf

        #V_stack = self.N_cells * V_cell  # Stack operational voltage -> this is combined in iv_calc for power rather than here

        return V_cell

    def dynamic_operation(self): #UNUSED
        """
        Model the electrolyzer's realistic response/operation under variable RE

        TODO: add this capability to the model
        """
        # When electrolyzer is already at or near its optimal operation
        # temperature (~80degC)
        warm_startup_time_secs = 30
        cold_startup_time_secs = 5 * 60  # 5 minutes

    def water_electrolysis_efficiency(self): #UNUSED
        """
        https://www.sciencedirect.com/science/article/pii/S2589299119300035#b0500

        According to the first law of thermodynamics energy is conserved.
        Thus, the conversion efficiency calculated from the yields of
        converted electrical energy into chemical energy. Typically,
        water electrolysis efficiency is calculated by the higher heating
        value (HHV) of hydrogen. Since the electrolysis process water is
        supplied to the cell in liquid phase efficiency can be calculated by:

        n_T = V_TN / V_cell

        where, V_TN is the thermo-neutral voltage (min. required V to
        electrolyze water)

        Parameters
        ______________

        Returns
        ______________

        """
        # From the source listed in this function ...
        # n_T=V_TN/V_cell NOT what's below which is input voltage -> this should call cell_design()
        n_T = self.V_TN / (self.stack_input_voltage_DC / self.N_cells)
        return n_T

    def faradaic_efficiency(self): #ONLY EFFICIENCY CONSIDERED RIGHT NOW
        """`
        Text background from:
        [https://www.researchgate.net/publication/344260178_Faraday%27s_
        Efficiency_Modeling_of_a_Proton_Exchange_Membrane_Electrolyzer_
        Based_on_Experimental_Data]

        In electrolyzers, Faraday’s efficiency is a relevant parameter to
        assess the amount of hydrogen generated according to the input
        energy and energy efficiency. Faraday’s efficiency expresses the
        faradaic losses due to the gas crossover current. The thickness
        of the membrane and operating conditions (i.e., temperature, gas
        pressure) may affect the Faraday’s efficiency.

        Equation for n_F obtained from:
        https://www.sciencedirect.com/science/article/pii/S0360319917347237#bib27

        Parameters
        ______________
        float f_1
            Coefficient - value at operating temperature of 80degC (mA2/cm4)

        float f_2
            Coefficient - value at operating temp of 80 degC (unitless)

        np_array current_input_external_Amps
            1-D array of current supplied to electrolyzer stack from external
            power source


        Returns
        ______________

        float n_F
            Faradaic efficiency (unitless)

        """
        f_1 = 250  # Coefficient (mA2/cm4)
        f_2 = 0.996  # Coefficient (unitless)
        I_cell = self.output_dict['current_input_external_Amps'] * 1000

        # Faraday efficiency
        n_F = (((I_cell / self.cell_active_area) ** 2) /
               (f_1 + ((I_cell / self.cell_active_area) ** 2))) * f_2

        return n_F

    def compression_efficiency(self): #UNUSED AND MAY HAVE ISSUES
        # Should this only be used if we plan on storing H2?
        """
        In industrial contexts, the remaining hydrogen should be stored at
        certain storage pressures that vary depending on the intended
        application. In the case of subsequent compression, pressure-volume
        work, Wc, must be performed. The additional pressure-volume work can
        be related to the heating value of storable hydrogen. Then, the total
        efficiency reduces by the following factor:
        https://www.mdpi.com/1996-1073/13/3/612/htm

        Due to reasons of material properties and operating costs, large
        amounts of gaseous hydrogen are usually not stored at pressures
        exceeding 100 bar in aboveground vessels and 200 bar in underground
        storages
        https://www.sciencedirect.com/science/article/pii/S0360319919310195

        Partial pressure of H2(g) calculated using:
        The hydrogen partial pressure is calculated as a difference between
        the  cathode  pressure, 101,325 Pa, and the water saturation
        pressure
        [Source: Energies2018,11,3273; doi:10.3390/en11123273]

        """
        n_limC = 0.825  # Limited efficiency of gas compressors (unitless)
        H_LHV = 241  # Lower heating value of H2 (kJ/mol)
        K = 1.4  # Average heat capacity ratio (unitless)
        C_c = 2.75  # Compression factor (ratio of pressure after and before compression)
        n_F = self.faradaic_efficiency()
        j = self.output_dict['stack_current_density_A_cm2']
        n_x = ((1 - n_F) * j) * self.cell_active_area
        n_h2 = j * self.cell_active_area
        Z = 1  # [Assumption] Average compressibility factor (unitless)
        T_in = 273.15 + self.T_C  # (Kelvins) Assuming electrolyzer operates at 80degC
        W_1_C = (K / (K - 1)) * ((n_h2 - n_x) / self.F) * self.R * T_in * Z * \
                ((C_c ** ((K - 1) / K)) - 1)  # Single stage compression

        # Calculate partial pressure of H2 at the cathode: This is the Antoine formula (see link below)
        #https://www.omnicalculator.com/chemistry/vapour-pressure-of-water#antoine-equation
        A = 8.07131
        B = 1730.63
        C = 233.426
        p_h2o_sat = 10 ** (A - (B / (C + self.T_C)))  # [mmHg]
        p_cat = 101325  # Cathode pressure (Pa)
        #Fixed unit bug between mmHg and Pa
        
        p_h2_cat = p_cat - (p_h2o_sat*self.mmHg_2_Pa) #convert mmHg to Pa
        p_s_h2_Pa = self.p_s_h2_bar * 1e5

        s_C = math.log((p_s_h2_Pa / p_h2_cat), 10) / math.log(C_c, 10)
        W_C = round(s_C) * W_1_C  # Pressure-Volume work - energy reqd. for compression
        net_energy_carrier = n_h2 - n_x  # C/s
        net_energy_carrier = np.where((n_h2 - n_x) == 0, 1, net_energy_carrier)
        n_C = 1 - ((W_C / (((net_energy_carrier) / self.F) * H_LHV * 1000)) * (1 / n_limC))
        n_C = np.where((n_h2 - n_x) == 0, 0, n_C)
        return n_C

    def total_efficiency(self):
        """
        Aside from efficiencies accounted for in this model
        (water_electrolysis_efficiency, faradaic_efficiency, and
        compression_efficiency) all process steps such as gas drying above
        2 bar or water pumping can be assumed as negligible. Ultimately, the
        total efficiency or system efficiency of a PEM electrolysis system is:

        n_T = n_p_h2 * n_F_h2 * n_c_h2
        https://www.mdpi.com/1996-1073/13/3/612/htm
        """
        #n_p_h2 = self.water_electrolysis_efficiency() #no longer considered
        n_F_h2 = self.faradaic_efficiency()
        #n_c_h2 = self.compression_efficiency() #no longer considered

        #n_T = n_p_h2 * n_F_h2 * n_c_h2 #No longer considers these other efficiencies
        n_T=n_F_h2
        self.output_dict['total_efficiency'] = n_T
        return n_T

    def h2_production_rate(self):
        """
        H2 production rate calculated using Faraday's Law of Electrolysis
        (https://www.sciencedirect.com/science/article/pii/S0360319917347237#bib27)

        Parameters
        _____________

        float f_1
            Coefficient - value at operating temperature of 80degC (mA2/cm4)

        float f_2
            Coefficient - value at operating temp of 80 degC (unitless)

        np_array
            1-D array of current supplied to electrolyzer stack from external
            power source


        Returns
        _____________

        """
        # Single stack calculations:
        n_Tot = self.total_efficiency()
        h2_production_rate = n_Tot * ((self.N_cells *
                                       self.output_dict['current_input_external_Amps']) /
                                      (2 * self.F))  # mol/s
        h2_production_rate_g_s = h2_production_rate / self.moles_per_g_h2
        h2_produced_kg_hr = h2_production_rate_g_s * 3.6 #Fixed: no more manual scaling
        self.output_dict['stack_h2_produced_g_s']= h2_production_rate_g_s
        self.output_dict['stack_h2_produced_kg_hr'] = h2_produced_kg_hr

        # Total electrolyzer system calculations:
        h2_produced_kg_hr_system = self.system_design() * h2_produced_kg_hr
        # h2_produced_kg_hr_system = h2_produced_kg_hr
        self.output_dict['h2_produced_kg_hr_system'] = h2_produced_kg_hr_system

        return h2_produced_kg_hr_system, h2_production_rate_g_s 

    def degradation(self):
        """
        TODO
        Add a time component to the model - for degradation ->
        https://www.hydrogen.energy.gov/pdfs/progress17/ii_b_1_peters_2017.pdf
        """
        pass

    def water_supply(self):
        """
        Calculate water supply rate based system efficiency and H2 production
        rate
        TODO: Add this capability to the model
        
        The 10x multiple is likely too low. See Lampert, David J., Cai, Hao, Wang, Zhichao, Keisman, Jennifer, Wu, May, Han, Jeongwoo, Dunn, Jennifer, Sullivan, John L., Elgowainy, Amgad, Wang, Michael, & Keisman, Jennifer. Development of a Life Cycle Inventory of Water Consumption Associated with the Production of Transportation Fuels. United States. https://doi.org/10.2172/1224980
        """
        # ratio of water_used:h2_kg_produced depends on power source
        # h20_kg:h2_kg with PV 22-126:1 or 18-25:1 without PV but considering water deminersalisation
        # stoichometrically its just 9:1 but ... theres inefficiencies in the water purification process
        max_water_feed_mass_flow_rate_kg_hr = 411  # kg per hour
        h2_produced_kg_hr_system, h2_production_rate_g_s = self.h2_production_rate() 
        water_used_kg_hr_system = h2_produced_kg_hr_system * 10
        self.output_dict['water_used_kg_hr'] = water_used_kg_hr_system
        self.output_dict['water_used_kg_annual'] = np.sum(water_used_kg_hr_system)

    def h2_storage(self):
        """
        Model to estimate Ideal Isorthermal H2 compression at 70degC
        https://www.sciencedirect.com/science/article/pii/S036031991733954X

        The amount of hydrogen gas stored under pressure can be estimated
        using the van der Waals equation

        p = [(nRT)/(V-nb)] - [a * ((n^2) / (V^2))]

        where p is pressure of the hydrogen gas (Pa), n the amount of
        substance (mol), T the temperature (K), and V the volume of storage
        (m3). The constants a and b are called the van der Waals coefficients,
        which for hydrogen are 2.45 × 10−2 Pa m6mol−2 and 26.61 × 10−6 ,
        respectively.
        """

        pass


if __name__=="__main__":
    # Example on how to use this model:
    in_dict = dict()
    in_dict['electrolyzer_system_size_MW'] = 15
    out_dict = dict()

    electricity_profile = pd.read_csv('sample_wind_electricity_profile.csv')
    in_dict['P_input_external_kW'] = electricity_profile.iloc[:, 1].to_numpy()

    el = PEM_electrolyzer_LT(in_dict, out_dict)
    el.h2_production_rate()
    print("Hourly H2 production by stack (kg/hr): ", out_dict['stack_h2_produced_kg_hr'][0:50])
    print("Hourly H2 production by system (kg/hr): ", out_dict['h2_produced_kg_hr_system'][0:50])
    fig, axs = plt.subplots(2, 2)
    fig.suptitle('PEM H2 Electrolysis Results for ' +
                str(out_dict['electrolyzer_system_size_MW']) + ' MW System')

    axs[0, 0].plot(out_dict['stack_h2_produced_kg_hr'])
    axs[0, 0].set_title('Hourly H2 production by stack')
    axs[0, 0].set_ylabel('kg_h2 / hr')
    axs[0, 0].set_xlabel('Hour')

    axs[0, 1].plot(out_dict['h2_produced_kg_hr_system'])
    axs[0, 1].set_title('Hourly H2 production by system')
    axs[0, 1].set_ylabel('kg_h2 / hr')
    axs[0, 1].set_xlabel('Hour')

    axs[1, 0].plot(in_dict['P_input_external_kW'])
    axs[1, 0].set_title('Hourly Energy Supplied by Wind Farm (kWh)')
    axs[1, 0].set_ylabel('kWh')
    axs[1, 0].set_xlabel('Hour')

    total_efficiency = out_dict['total_efficiency']
    system_h2_eff = (1 / total_efficiency) * 33.3
    system_h2_eff = np.where(total_efficiency == 0, 0, system_h2_eff)

    axs[1, 1].plot(system_h2_eff)
    axs[1, 1].set_title('Total Stack Energy Usage per mass net H2')
    axs[1, 1].set_ylabel('kWh_e/kg_h2')
    axs[1, 1].set_xlabel('Hour')

    plt.show()
    print("Annual H2 production (kg): ", np.sum(out_dict['h2_produced_kg_hr_system']))
    print("Annual energy production (kWh): ", np.sum(in_dict['P_input_external_kW']))
    print("H2 generated (kg) per kWH of energy generated by wind farm: ",
          np.sum(out_dict['h2_produced_kg_hr_system']) / np.sum(in_dict['P_input_external_kW']))