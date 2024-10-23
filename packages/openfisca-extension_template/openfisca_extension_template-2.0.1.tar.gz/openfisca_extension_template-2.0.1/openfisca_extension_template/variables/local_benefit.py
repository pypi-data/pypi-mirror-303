"""This file defines an additional variable for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See:
    https://openfisca.org/doc/key-concepts/variables.html

"""

# Import the openfisca-core objects used to code the legislation in OpenFisca.
from openfisca_core.periods import MONTH
from openfisca_core.variables import Variable

# Import the entities specifically defined for this tax and benefit system.
from openfisca_country_template.entities import Household


class local_town_child_allowance(Variable):
    value_type = float
    entity = Household
    definition_period = MONTH
    label = "Local benefit: a fixed amount by child each month"

    def formula(family, period, parameters):
        """Local benefit.

        Extensions can only add variables and parameters to the tax and benefit
        system: they cannot modify or neutralize existing ones.

        Args:
            family: a population of entities.
            period: an `Instant` to calculate the variable.
            parameters: a bounded function to query for model's parameters.

        Returns:
            A vector with the corresponding values per entity.

        """
        nb_children = family.nb_persons(role=Household.CHILD)
        amount_by_child = parameters(period).local_town.child_allowance.amount
        return nb_children * amount_by_child
