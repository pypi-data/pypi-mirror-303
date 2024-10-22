from django.db.models import Prefetch, Q, QuerySet

from aleksis.core.managers import AlekSISBaseManagerWithoutMigrations
from aleksis.core.models import Person


class EvaluationPhaseManager(AlekSISBaseManagerWithoutMigrations):
    """Manager adding specific methods to evaluation phases."""

    def get_queryset(self):
        """Ensure all related data is loaded as well."""
        return super().get_queryset().select_related("evaluated_group")


class EvaluationPhaseQuerySet(QuerySet):
    """Custom QuerySet for evaluation phases."""

    def for_person(self, person: Person) -> "EvaluationPhaseQuerySet":
        return self.filter(evaluated_group__members=person)

    def not_registered(self, person: Person) -> "EvaluationPhaseQuerySet":
        return self.exclude(registrations__person=person)

    def can_register(self, person: Person) -> "EvaluationPhaseQuerySet":
        return self.for_person(person).not_registered(person)

    def for_person_with_registrations(self, person: Person) -> "EvaluationPhaseQuerySet":
        from aleksis.apps.evalu.models import EvaluationRegistration

        return self.for_person(person).prefetch_related(
            Prefetch(
                "registrations",
                queryset=EvaluationRegistration.objects.filter(person=person),
            )
        )


class EvaluationRegistrationManager(AlekSISBaseManagerWithoutMigrations):
    """Manager adding specific methods to evaluation registrations."""

    def get_queryset(self):
        """Ensure all related data is loaded as well."""
        return super().get_queryset().select_related("phase", "person", "keys")


class EvaluationRegistrationQuerySet(QuerySet):
    """Custom QuerySet for evaluation registrations."""


class EvaluationGroupManager(AlekSISBaseManagerWithoutMigrations):
    """Manager adding specific methods to evaluation groups."""

    def get_queryset(self):
        """Ensure all related data is loaded as well."""
        return super().get_queryset().select_related("registration", "group")


class EvaluationGroupQuerySet(QuerySet):
    """Custom QuerySet for evaluation groups."""

    def for_person(self, person: Person) -> "EvaluationGroupQuerySet":
        """Get all groups for which a person can evaluate."""
        return self.filter(Q(group__members=person) | Q(done_evaluations__evaluated_by=person))

    def for_person_with_done_evaluations(self, person: Person) -> "EvaluationGroupQuerySet":
        from aleksis.apps.evalu.models import DoneEvaluation

        return self.for_person(person).prefetch_related(
            Prefetch(
                "done_evaluations",
                queryset=DoneEvaluation.objects.filter(evaluated_by=person),
            )
        )
