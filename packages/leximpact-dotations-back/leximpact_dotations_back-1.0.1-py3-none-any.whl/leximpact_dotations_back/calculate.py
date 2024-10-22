import logging

from openfisca_core.errors.variable_not_found_error import VariableNotFoundError
from openfisca_core.simulation_builder import SimulationBuilder
from openfisca_france_dotations_locales import (
    CountryTaxBenefitSystem as OpenFiscaFranceDotationsLocales,
)


CURRENT_YEAR = 2024
model = OpenFiscaFranceDotationsLocales()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def set_simulation_inputs(simulation, data, period):
    for champ_openfisca in data.columns:
        try:
            simulation.tax_benefit_system.get_variable(champ_openfisca, check_existence=True)
            # oui c'est comme ça que je checke qu'une variable est openfisca ne me jugez pas
            # si exception, on choisit d'arrêter l'application
            simulation.set_input(
                champ_openfisca,
                period,
                data[champ_openfisca],
            )
        except VariableNotFoundError as e:
            logger.fatal("Error while setting up this year data.")
            raise e

    return simulation


def set_simulation_previous_year_inputs(simulation, data_current_year, data_previous_year, period):
    # data_previous_year est un dataframe dont toutes les colonnes
    # portent des noms de variables openfisca
    # et contiennent des valeurs de l'an dernier.

    if data_previous_year is not None:
        # on rassemble les informations de l'an dernier pour les communes
        # qui existent aussi cette année (les valeurs des nouvelles communes sont à zéro)

        # TODO vérifier qu'il ne s'agit pas d'une commune nouvelle ; exemple limite actuelle :
        # on se base sur le code INSEE qui peut être identique d'une année à l'autre
        # alors que la commune a fusionné avec une autre
        full_data = data_current_year.merge(
            data_previous_year,
            on="code_insee",
            how="left",
            suffixes=["_currentyear", ""],
        )

        for champ_openfisca in data_previous_year.columns:
            try:
                # oui c'est comme ça que je checke qu'une variable est openfisca ne me jugez pas
                # si exception, on choisit d'arrêter l'application
                simulation.tax_benefit_system.get_variable(champ_openfisca, check_existence=True)

                simulation.set_input(
                    champ_openfisca,
                    str(int(period) - 1),
                    full_data[champ_openfisca].fillna(0),
                )
            except VariableNotFoundError as e:
                logger.fatal("Error while setting up previous year data.")
                raise e

    return simulation


def create_simulation_with_data(model, period, data, data_previous_year=None):
    sb = SimulationBuilder()
    sb.create_entities(model)
    sb.declare_person_entity("commune", data.index)

    etat_instance = sb.declare_entity("etat", ["france"])
    nombre_communes = len(data.index)
    etat_communes = ["france"] * nombre_communes
    communes_etats_roles = [None] * nombre_communes  # no roles in our model
    sb.join_with_persons(etat_instance, etat_communes, communes_etats_roles)

    simulation = sb.build(model)

    # TODO vérifier nécessité : simulation.max_spiral_loops = 10

    simulation = set_simulation_inputs(simulation, data, period)
    if data_previous_year is None:
        logger.warning("Creating simulation without previous year data.")
    else:
        simulation = set_simulation_previous_year_inputs(simulation, data, data_previous_year, period)

    return simulation
