# https://www.kaggle.com/datasets/podsyp/production-quality/
# https://www.kaggle.com/datasets/mmelahi/cheminformatics/data
# https://www.kaggle.com/datasets/inIT-OWL/production-plant-data-for-condition-monitoring IMPROVE
# https://www.kaggle.com/datasets/supergus/multistage-continuousflow-manufacturing-process
# https://www.bigdata-ai.fraunhofer.de/s/datasets/index.html


# continuous_factory_process
# https://www.kaggle.com/datasets/supergus/multistage-continuousflow-manufacturing-process


from typing import Tuple
#from kutec.common import get_definition, get_quality
#from kutec.sample_generation.sample_writer import SampleWriter
from ..example import Example


class FactoryProcessExample(Example):
    def __init__(self):
        self.manipulatable_features_dict = {
            'CWW_to_SOP_centr': [0.0, 5.0, 1],
            'Temp_SOP_reactor_R015': [44.0, 52.0, 1],
            'Vol._Flow_hot_proc_water_to_SOP_reactor_R015_': [0.8, 2.0, 1],
            'CWW_to_Schoenite_centr_1': [0.0, 5.0, 1],
            'CWW_to_Schoenite_centr_2': [0.0, 5.0, 1],
            'Flow_Transm_CWW_to_Schoenite_centr_CE180.2': [0.0, 5.0, 1],
            'Flow_Transm_CWW_to_Schoenite_centr_CE180.1': [0.0, 5.0, 1],
            'FlowTransm_CWW_to_centr': [0.0, 5.0, 1],
            'Flow_Transm_for_Proc_water_Tailingsslurry_vessel_V220': [0.0, 30.0, 1],
            'Flow_to_flot_cell_1': [280.0, 360.0, 2],
            'Water_supply_V090': [0.0, 10.0, 1],
            'Feed_Transm_procwater_R010': [0.0, 20.0, 1],
            'Mass_stream_C040_(Mass_stream_raw_KTMS)': [22.6, 126.0, 1],
            'R030_OF_silds_Fraction': [0.0, 10.0, 2],
            'R030_UF_Solids_Fraction': [25.0, 50.0, 2],
            'V050_OF_solids_Fraction': [0.0, 5.0, 2],
            'V050_UF_solids_Fraction': [5.0, 40.0, 2],
            'Ratio_R030_UF_and_Schönite_ML': [0.5, 1.5, 2],
            'Yellow_Hose': [0.0, 20.0, 2],
            'S240_OF_solids_Fraction': [0.0, 10.0, 3],
            'S240_UF_solids_Fraction': [25.0, 50.0, 3],
            'CE250_Filtrate_solids_fraction': [0.0, 20.0, 3],
            'CE180-1_Filtrate_solids_fraction': [0.0, 20.0, 3],
            'CE180-2_Filtrate_solids_fraction': [0.0, 20.0, 3],
            'CE220-1_Filtrate_solids_fraction': [0.0, 20.0, 3],
            'CE220-2_Filtrate_solids_fraction': [0.0, 20.0, 3],
            'C220_Bypass': [0.0, 80.0, 2],
            'Breather_recycle': [0.0, 80.0, 2],
            'R015_OF_solids_fraction': [0.0, 10.0, 2],
            'R015_UF_solids_fraction': [15.0, 40.0, 2],
            'V080_OF_solids_fraction': [0.0, 5.0, 2],
            'V080_UF_solids_fraction': [0.0, 30.0, 2],
            'S120_OF_solids_frcation': [0.0, 10.0, 3],
            'S120_UF_solids_fraction': [30.0, 60.0, 3],
            'CE160_Filtrate_solids_fraction': [0.0, 20.0, 3],
            'Flot_Eff_CaSO4.H2O': [0.0, 50.0, 3],
            'Flot_Eff_K2SO4.CaSO4.H2O': [0.0, 50.0, 3],
            'Flot_Eff_K2SO4.MgSO4.4H2O': [22.0, 95.0, 3],
            'Flot_Eff_K2SO4.MgSO4.6H2O': [22.0, 95.0, 3],
            'Flot_Eff_K2SO4.MgSO4.CaSO4.2H2O': [0.0, 50.0, 3],
            'Flot_Eff_MgSO4.H2O': [0.0, 15.0, 3],
            'Flot_Eff_Na2SO4.3K2SO4': [0.0, 15.0, 3],
            'Flot_Eff_Insoluble': [22.0, 90.0, 3],
            'Concentr_NaCl_Concentrate': [2.0, 8.0, 3],
            'OF_Solids_Fraction_Flot': [25.0, 40.0, 3],
            'Ratio_ML_per_KTMS': [0.75, 2.0, 2],
            'Temp_Water_to_V220': [7.5, 25.5, 1],
            'Water_to_SOP_Dust': [0.2, 75.0, 1],
            'Proc_Water_to_2240-V010': [0.0, 0.0, 4],
            'Blue_lane_to_2250-V100': [0.0, 0.0, 4],
            'Bittern_to_2250-V050': [0.0, 0.0, 4],
            'Vol_Flow_cold_proc_water_to_SOP_reactor_R015': [0.0, 0.0, 4],
            'MgSO4*7H2O_content_KTMS': [0.0, 0.0, 4],
            'MgCl2*6H2O_content_KTMS': [0.0, 0.0, 4],
            'Schönit_ML_for_Flushing_P085': [0.0, 0.0, 4],
            'Schoenite_ML_To_2230-V150': [0.0, 0.0, 4],
            'Amount_Lilaflot': [50.0, 50.0, 4],
            'Concentr_Lilaflot': [4.4, 4.4, 4],
            'Flow_from_V220_to_V200': [0.0, 0.0, 4],
            'Dust_solution_to_V100': [0.0, 0.0, 4]
        }
        self.y_limits = {
            "Mass_SOP_per_Mass_KTMS": 0.2,
            "K_content_C330-solid": 50.0,
            "Na_content_C330-solid": 4.75,
            "Mg_content_C330-solid": 4.75,
            "S_content_C330-solid": 22.0,
            "Cl_content_C330-solid": 1.1
        }
        self.quality_thresholds = {
            "K_content_C330-solid": 42.336,
            "S_content_C330-solid": 18.023,
            "Cl_content_C330-solid": 1.0
        }
        self.normalization = "min_max"

    def get_constraints(self, x_0,
                        max_num_adaptations: int = -1,
                        epsilon: float = 1e-12) -> tuple:

        def flot_eff_h2o_constraint_a(x_values):
            #"Flot_Eff_CaSO4.H2O" == "Flot_Eff_K2SO4.CaSO4.H2O"
            Flot_Eff_CaSO4_H2O_idx = 55
            Flot_Eff_K2SO4_CaSO4_H2O_idx = 56
            return x_values[Flot_Eff_CaSO4_H2O_idx] - x_values[Flot_Eff_K2SO4_CaSO4_H2O_idx]

        def flot_eff_h2o_constraint_b(x_values):
            #"Flot_Eff_CaSO4.H2O" == "Flot_Eff_K2SO4.MgSO4.CaSO4.2H2O"
            Flot_Eff_CaSO4_H2O_idx = 55
            Flot_Eff_K2SO4_MgSO4_CaSO4_2H2O_idx = 59
            return x_values[Flot_Eff_CaSO4_H2O_idx] - x_values[Flot_Eff_K2SO4_MgSO4_CaSO4_2H2O_idx]

        def filtrate_solids_ce180(x_values):
            #"CE180-1_Filtrate_solids_fraction" == "CE180-2_Filtrate_solids_fraction"
            CE180_1_Filtrate_solids_fraction_idx = 28
            CE180_2_Filtrate_solids_fraction_idx = 31
            return x_values[CE180_1_Filtrate_solids_fraction_idx] - x_values[CE180_2_Filtrate_solids_fraction_idx]

        def filtrate_solids_ce220(x_values):
            #"CE220-1_Filtrate_solids_fraction" == "CE220-2_Filtrate_solids_fraction"
            CE220_1_Filtrate_solids_fraction_idx = 35
            CE220_2_Filtrate_solids_fraction_idx = 38
            return x_values[CE220_1_Filtrate_solids_fraction_idx] - x_values[CE220_2_Filtrate_solids_fraction_idx]

        def temp_water_v220_equals_proc_water(x_values):
            # TODO: this simplification restricts to aloow usage of process water only
            # forbids option to add 8 degrees cold water
            #"Temp_Water_to_V220" == "Temp_Proc_Water"
            Temp_Water_to_V220_idx = 67
            Temp_Proc_Water_idx = 5
            return x_values[Temp_Water_to_V220_idx] - x_values[Temp_Proc_Water_idx]

        def max_adaptations(x_values,
                            x_0,
                            max_num_adaptations,
                            epsilon: float = 1e-12):
            num_changed = 0
            for i, x_0_value in enumerate(x_0):
                num_changed += int(abs(x_values[i] - x_0_value) > epsilon)
            return -(num_changed - max_num_adaptations)

        constraints = [{
            'type': 'eq',
            'fun': flot_eff_h2o_constraint_a
        }, {
            'type': 'eq',
            'fun': flot_eff_h2o_constraint_b
        }, {
            'type': 'eq',
            'fun': filtrate_solids_ce180
        }, {
            'type': 'eq',
            'fun': filtrate_solids_ce220
        }, {
            'type': 'eq',
            'fun': temp_water_v220_equals_proc_water
        }]
        if max_num_adaptations > -1:
            x_0_values = list(x_0.values.flatten())
            constraints.append({
                'type': 'ineq',
                'fun': max_adaptations,
                'args': [x_0_values, max_num_adaptations, epsilon]
            })

        return tuple(constraints)


    def get_manipulatable_features(self) -> dict:
        return self.manipulatable_features_dict


    def _get_sop_k_s_cl(self, output: list) -> Tuple[float, float, float, float]:
        if len(output) == 4:
            sop, kalium, sulfur, chlor = output
        elif len(output) == 6:
            sop, kalium, _, _, sulfur, chlor = output
        else:
            raise RuntimeError(f"Cannot predict quality for output: {output}")
        return sop, kalium, sulfur, chlor


    def get_quality_str(self, output_denormalized: list) -> str:
        sop, kalium, sulfur, chlor = self._get_sop_k_s_cl(output_denormalized)
        quality = get_quality(chlor=chlor, kalium=kalium, sulfur=sulfur)

        quantity_str = f"SOP_per_KTMS={sop:.3f}"
        components_str = f"K={kalium:.3f}, S={sulfur:.3f}, Cl={chlor:.3f}"
        quality_str = "OK" if quality == 1.0 else "not OK"

        return f"{quantity_str}, {components_str} -> Product Quality: {quality_str}"


    def eval_objective(self, pred):
        sop, kalium, sulfur, chlor = self._get_sop_k_s_cl(pred)
        result = sop + kalium + sulfur - chlor
        return -result


    def write_samples_to_csv(self, sample_features: list, template: str, output_path: str) -> None:
        writer = SampleWriter(template, output_path)
        writer.write(sample_features)
