import dataclasses
import typing

from collections import defaultdict, Counter

import hpotk

from gpsea.model import Patient, Sex

from .._api import Categorization, PatientCategory
from ._api import GenotypePolyPredicate
from ._api import VariantPredicate
from ._counter import AlleleCounter
from ._variant import VariantPredicates


class AlleleCountingGroupsPredicate(GenotypePolyPredicate):
    # NOT PART OF THE PUBLIC API

    def __init__(
        self,
        counters: typing.Iterable[AlleleCounter],
        categorizations: typing.Iterable[Categorization],
    ):
        self._counters = tuple(counters)
        self._categorizations = tuple(categorizations)
        self._question = "Genotype group"

    def get_categorizations(self) -> typing.Sequence[Categorization]:
        return self._categorizations

    def get_question_base(self) -> str:
        return self._question

    def test(self, patient: Patient) -> typing.Optional[Categorization]:
        self._check_patient(patient)

        nonzero_counter_idxs = []
        for i, counter in enumerate(self._counters):
            allele_count = counter.count(patient)
            if allele_count > 0:
                nonzero_counter_idxs.append(i)

        if len(nonzero_counter_idxs) == 1:
            return self._categorizations[nonzero_counter_idxs[0]]
        else:
            # Patient can be assigned either into no group or into multiple groups.
            return None

    def __eq__(self, value: object) -> bool:
        return (
            isinstance(value, AlleleCountingGroupsPredicate)
            and self._counters == value._counters
            and self._categorizations == value._categorizations
        )

    def __hash__(self) -> int:
        return hash(
            (
                self._counters,
                self._categorizations,
            )
        )

    def __str__(self) -> str:
        return self.get_question_base()

    def __repr__(self) -> str:
        return (
            "AlleleCountingGroupsPredicate("
            + "counters={self._counters}, "
            + "categorizations={self._categorizations})"
        )


def groups_predicate(
    predicates: typing.Iterable[VariantPredicate],
    group_names: typing.Iterable[str],
) -> GenotypePolyPredicate:
    """
    Create a genotype predicate that bins the patient into one of *n* groups.

    The genotype groups *should* not overlap.
    In case of an overlap, the patient will be assigned into no group (`None`).

    See the :ref:`groups-predicate` section for an example.

    :param predicates: an iterable with at least 2 variant predicates to determine a genotype group.
    :param group_names: an iterable with group names. The number of group names must match the number of predicates.
    """
    # First, collect the iterables and check sanity.
    predicates = tuple(predicates)
    group_names = tuple(group_names)

    assert len(predicates) >= 2, f"We need at least 2 predicates: {len(predicates)}"
    assert len(predicates) == len(
        group_names
    ), f"The number of group names must match the number of predicates: {len(group_names)}!={len(predicates)}"

    # Then, prepare the counters and categorizations.
    counters = [AlleleCounter(predicate=predicate) for predicate in predicates]

    categorizations = []
    for i, (predicate, name) in enumerate(zip(predicates, group_names)):
        categorization = Categorization.from_raw_parts(
            cat_id=i,
            name=name,
            description=predicate.get_question(),
        )
        categorizations.append(categorization)

    # Last, put the predicate together.
    return AlleleCountingGroupsPredicate(
        counters=counters,
        categorizations=categorizations,
    )


def fixate_partitions(
    partitions: typing.Collection[typing.Collection[int]],
) -> typing.Collection[typing.Sequence[int]]:
    fixed = []
    for partition in partitions:
        fixed.append(tuple(partition))
    return fixed


def qc_partitions(
    partitions: typing.Collection[typing.Collection[int]],
):
    # NOT PART OF THE PUBLIC API

    # Outer element is a collection
    if not isinstance(partitions, typing.Collection):
        raise ValueError("Partitions must be a collection")
    # Inner elements are all collections ...
    if not all(isinstance(partition, typing.Collection) for partition in partitions):
        raise ValueError("Each partition must be a collection")
    # ... we must have at least 2 partitions ...
    if not len(partitions) >= 2:
        raise ValueError("At least 2 partitions must be provided")
    # ... and the inner collection elements are all ints
    if not all(
        isinstance(e, int) and e >= 0 for partition in partitions for e in partition
    ):
        raise ValueError("Each partition index must be a non-negative int")

    # Each partition must be unique ...
    partition_counter = Counter(partitions)
    errors = []
    for partition, count in partition_counter.items():
        if count > 1:
            errors.append(f"partition {partition} was present {count}!=1 times")
    if len(errors) > 0:
        raise ValueError(", ".join(errors))

    # ... and each index/element must be unique as well
    element_counter = Counter(e for partition in partitions for e in partition)
    errors = []
    for element, count in element_counter.items():
        if count > 1:
            errors.append(f"element {element} was present {count}!=1 times")
    if len(errors) > 0:
        raise ValueError(", ".join(errors))


def build_count_to_cat(
    a_label: str,
    b_label: str,
    partitions: typing.Iterable[typing.Iterable[int]],
) -> typing.Mapping[typing.Tuple[int, int], Categorization]:
    # NOT PART OF THE PUBLIC API
    partition2ac = (
        (2, 0),
        (1, 1),
        (0, 2),
    )

    partition2label = (
        f"{a_label}/{a_label}",
        f"{a_label}/{b_label}",
        f"{b_label}/{b_label}",
    )

    ac2cat = {}
    for i, partition in enumerate(partitions):
        label = " OR ".join(partition2label[j] for j in partition)

        cat = Categorization(
            PatientCategory(cat_id=i, name=label, description=label),
        )
        for id in partition:
            ac = partition2ac[id]
            ac2cat[ac] = cat

    return ac2cat


def deduplicate_categorizations(
    cats: typing.Iterable[Categorization],
) -> typing.Sequence[Categorization]:
    return sorted(
        set(cats),
        key=lambda c: c.category.cat_id,
    )


class PolyCountingGenotypePredicate(GenotypePolyPredicate):
    # NOT PART OF THE PUBLIC API

    @staticmethod
    def monoallelic(
        a_predicate: VariantPredicate,
        b_predicate: VariantPredicate,
        a_label: str,
        b_label: str,
    ) -> "PolyCountingGenotypePredicate":
        count2cat = {
            (1, 0): Categorization(
                PatientCategory(
                    cat_id=0, name=a_label, description=f"Monoallelic {a_label}"
                )
            ),
            (0, 1): Categorization(
                PatientCategory(
                    cat_id=1, name=b_label, description=f"Monoallelic {b_label}"
                )
            ),
        }

        return PolyCountingGenotypePredicate.for_predicates_and_categories(
            count2cat=count2cat,
            a_predicate=a_predicate,
            b_predicate=b_predicate,
        )

    @staticmethod
    def biallelic(
        a_predicate: VariantPredicate,
        b_predicate: VariantPredicate,
        a_label: str,
        b_label: str,
        partitions: typing.Iterable[typing.Iterable[int]],
    ) -> "PolyCountingGenotypePredicate":
        count2cat = build_count_to_cat(
            a_label=a_label,
            b_label=b_label,
            partitions=partitions,
        )

        return PolyCountingGenotypePredicate.for_predicates_and_categories(
            count2cat=count2cat,
            a_predicate=a_predicate,
            b_predicate=b_predicate,
        )

    @staticmethod
    def for_predicates_and_categories(
        count2cat: typing.Mapping[typing.Tuple[int, int], Categorization],
        a_predicate: VariantPredicate,
        b_predicate: VariantPredicate,
    ) -> "PolyCountingGenotypePredicate":
        return PolyCountingGenotypePredicate(
            a_counter=AlleleCounter(a_predicate),
            b_counter=AlleleCounter(b_predicate),
            count2cat=count2cat,
        )

    def __init__(
        self,
        count2cat: typing.Mapping[typing.Tuple[int, int], Categorization],
        a_counter: AlleleCounter,
        b_counter: AlleleCounter,
    ):
        self._count2cat = dict(count2cat)
        self._categorizations = tuple(deduplicate_categorizations(count2cat.values()))
        self._a_counter = a_counter
        self._b_counter = b_counter
        self._hash = self._compute_hash()

    def _compute_hash(self) -> int:
        hash_value = 17

        self._groups = defaultdict(list)
        for count, cat in self._count2cat.items():
            hash_value += 13 * hash(count)
            hash_value += 13 * hash(cat)

        hash_value += 23 * hash(self._a_counter)
        hash_value += 23 * hash(self._b_counter)

        return hash_value

    def get_categorizations(self) -> typing.Sequence[Categorization]:
        return self._categorizations

    def get_question_base(self) -> str:
        return "Allele group"

    def test(self, patient: Patient) -> typing.Optional[Categorization]:
        self._check_patient(patient)

        a_count = self._a_counter.count(patient)
        b_count = self._b_counter.count(patient)
        counts = (a_count, b_count)

        return self._count2cat.get(counts, None)

    def __eq__(self, value: object) -> bool:
        return (
            isinstance(value, PolyCountingGenotypePredicate)
            and self._count2cat == value._count2cat
            and self._a_counter == value._a_counter
            and self._b_counter == value._b_counter
        )

    def __hash__(self) -> int:
        return self._hash


def monoallelic_predicate(
    a_predicate: VariantPredicate,
    b_predicate: VariantPredicate,
    a_label: str = "A",
    b_label: str = "B",
) -> GenotypePolyPredicate:
    """
    The predicate bins patient into one of two groups, `A` and `B`,
    based on presence of *exactly* one allele of a variant
    that meets the predicate criteria.

    See :ref:`monoallelic-predicate` for more information and an example usage.

    :param a_predicate: predicate to test if the variants
        meet the criteria of the first group (named `A` by default).
    :param b_predicate: predicate to test if the variants
        meet the criteria of the second group (named `B` by default).
    :param a_label: display name of the `a_predicate` (default ``"A"``).
    :param b_label: display name of the `b_predicate` (default ``"B"``).
    """
    assert isinstance(a_label, str)
    assert isinstance(b_label, str)

    return PolyCountingGenotypePredicate.monoallelic(
        a_predicate=a_predicate,
        b_predicate=b_predicate,
        a_label=a_label,
        b_label=b_label,
    )


def biallelic_predicate(
    a_predicate: VariantPredicate,
    b_predicate: VariantPredicate,
    a_label: str = "A",
    b_label: str = "B",
    partitions: typing.Collection[typing.Collection[int]] = ((0,), (1,), (2,)),
) -> GenotypePolyPredicate:
    """
    The predicate bins patient into one of the three groups,
    `AA`, `AB`, and `BB`,
    based on presence of *two* variant alleles
    that meet the predicate criteria.

    See :ref:`biallelic-predicate` for more information and an example usage.

    :param a_predicate: predicate to test if the variants meet the criteria of the first group (named `A` by default).
    :param b_predicate: predicate to test if the variants meet the criteria of the second group (named `B` by default).
    :param a_label: display name of the `a_predicate` (default ``"A"``).
    :param b_label: display name of the `b_predicate` (default ``"B"``).
    :param partitions: a sequence with partition identifiers (default ``((0,), (1,), (2,))``).
    """
    # Q/C
    assert isinstance(a_label, str)
    assert isinstance(b_label, str)

    partitions = fixate_partitions(partitions)
    qc_partitions(partitions)

    return PolyCountingGenotypePredicate.biallelic(
        a_predicate=a_predicate,
        b_predicate=b_predicate,
        a_label=a_label,
        b_label=b_label,
        partitions=partitions,
    )


def autosomal_dominant(
    variant_predicate: typing.Optional[VariantPredicate] = None,
) -> GenotypePolyPredicate:
    """
    Create a predicate that assigns the patient either
    into homozygous reference or heterozygous
    group in line with the autosomal dominant mode of inheritance.

    See :ref:`mode-of-inheritance-predicate` for more info and an example usage.

    :param variant_predicate: a predicate for choosing the variants for testing
        or `None` if all variants should be used.
    """
    if variant_predicate is None:
        variant_predicate = VariantPredicates.true()

    return ModeOfInheritancePredicate.from_moi_info(
        variant_predicate=variant_predicate,
        mode_of_inheritance_data=ModeOfInheritanceInfo.autosomal_dominant(),
        partitions=((0,), (1,)),
    )


def autosomal_recessive(
    variant_predicate: typing.Optional[VariantPredicate] = None,
    partitions: typing.Collection[typing.Collection[int]] = ((0,), (1,), (2,)),
) -> GenotypePolyPredicate:
    """
    Create a predicate that assigns the patient either into
    homozygous reference, heterozygous, or biallelic alternative allele
    (homozygous alternative or compound heterozygous)
    group in line with the autosomal recessive mode of inheritance.

    See :ref:`mode-of-inheritance-predicate` for more info and an example usage.

    :param variant_predicate: a predicate for choosing the variants for testing
        or `None` if all variants should be used
    :param partitions: a sequence with partition identifiers (default ``((0,), (1,), (2,))``).
    """
    if variant_predicate is None:
        variant_predicate = VariantPredicates.true()

    partitions = fixate_partitions(partitions)

    return ModeOfInheritancePredicate.from_moi_info(
        variant_predicate=variant_predicate,
        mode_of_inheritance_data=ModeOfInheritanceInfo.autosomal_recessive(),
        partitions=partitions,
    )


@dataclasses.dataclass(frozen=True)
class GenotypeGroup:
    allele_count: int
    sex: typing.Optional[Sex]
    categorization: Categorization


class ModeOfInheritanceInfo:

    # NOT PART OF THE PUBLIC API!!!

    HOM_REF = Categorization(
        PatientCategory(
            cat_id=0,
            name="No allele",
            description="No allele",
        ),
    )
    HET = Categorization(
        PatientCategory(
            cat_id=1,
            name="Monoallelic",
            description="Monoallelic",
        ),
    )
    BIALLELIC_ALT = Categorization(
        PatientCategory(
            cat_id=2,
            name="Biallelic",
            description="Homozygous alternate or compound heterozygous",
        ),
    )

    @staticmethod
    def autosomal_dominant() -> "ModeOfInheritanceInfo":
        groups = (
            GenotypeGroup(
                allele_count=0,
                sex=None,
                categorization=ModeOfInheritanceInfo.HOM_REF,
            ),
            GenotypeGroup(
                allele_count=1,
                sex=None,
                categorization=ModeOfInheritanceInfo.HET,
            ),
        )
        return ModeOfInheritanceInfo(
            groups=groups,
        )

    @staticmethod
    def autosomal_recessive() -> "ModeOfInheritanceInfo":
        groups = (
            GenotypeGroup(
                allele_count=0,
                sex=None,
                categorization=ModeOfInheritanceInfo.HOM_REF,
            ),
            GenotypeGroup(
                allele_count=1,
                sex=None,
                categorization=ModeOfInheritanceInfo.HET,
            ),
            GenotypeGroup(
                allele_count=2,
                sex=None,
                categorization=ModeOfInheritanceInfo.BIALLELIC_ALT,
            ),
        )
        return ModeOfInheritanceInfo(
            groups=groups,
        )

    def __init__(
        self,
        groups: typing.Iterable[GenotypeGroup],
    ):
        # We want this to be hashable but also keep a non-hashable dict
        # as a field. Therefore, we pre-compute the hash manually.
        # The correctness depends on two default dicts with same keys and values
        # comparing equal.
        hash_value = 17

        self._groups = defaultdict(list)
        for group in groups:
            assert isinstance(group, GenotypeGroup)
            self._groups[group.allele_count].append(group)
            hash_value += 13 * hash(group)

        self._hash = hash_value

    @property
    def groups(self) -> typing.Iterator[GenotypeGroup]:
        # Flatten `values()` which is an iterable of lists.
        return (group for meta_group in self._groups.values() for group in meta_group)

    def get_groups_for_allele_count(
        self,
        allele_count: int,
    ) -> typing.Sequence[GenotypeGroup]:
        try:
            return self._groups[allele_count]
        except KeyError:
            # No group for this allele count is OK
            return ()

    def __eq__(self, value: object) -> bool:
        return (
            isinstance(value, ModeOfInheritanceInfo) and self._groups == value._groups
        )

    def __hash__(self) -> int:
        return self._hash

    def __str__(self) -> str:
        return f"ModeOfInheritanceInfo(groups={self._groups})"

    def __repr__(self) -> str:
        return str(self)


class ModeOfInheritancePredicate(GenotypePolyPredicate):
    # NOT PART OF THE PUBLIC API!!!
    """
    `ModeOfInheritancePredicate` assigns an individual into a group based on compatibility with
    the selected mode of inheritance.
    """

    @staticmethod
    def from_moi_info(
        variant_predicate: VariantPredicate,
        mode_of_inheritance_data: ModeOfInheritanceInfo,
        partitions: typing.Collection[typing.Collection[int]],
    ) -> "ModeOfInheritancePredicate":
        """
        Create a predicate for specified mode of inheritance data.
        """
        qc_partitions(partitions=partitions)

        allele_counter = AlleleCounter(predicate=variant_predicate)
        count2cat = ModeOfInheritancePredicate.prepare_count2cat(
            mode_of_inheritance_data=mode_of_inheritance_data,
            partitions=partitions,
        )
        return ModeOfInheritancePredicate(
            allele_counter=allele_counter,
            count2cat=count2cat,
        )

    @staticmethod
    def prepare_count2cat(
        mode_of_inheritance_data: ModeOfInheritanceInfo,
        partitions: typing.Collection[typing.Collection[int]],
    ) -> typing.Mapping[int, Categorization]:
        groups = tuple(mode_of_inheritance_data.groups)
        partition_to_allele_count = tuple(range(len(groups)))
        partition_to_label = tuple(
            group.categorization.category.name for group in groups
        )

        count2cat = {}
        for i, partition in enumerate(partitions):
            label = " OR ".join(partition_to_label[j] for j in partition)

            cat = Categorization(
                PatientCategory(
                    cat_id=i,
                    name=label,
                    description=label,
                )
            )
            for p in partition:
                allele_count = partition_to_allele_count[p]
                count2cat[allele_count] = cat

        return count2cat

    def __init__(
        self,
        allele_counter: AlleleCounter,
        count2cat: typing.Mapping[int, Categorization],
    ):
        assert isinstance(allele_counter, AlleleCounter)
        self._allele_counter = allele_counter

        self._count2cat = dict(count2cat)
        self._categorizations = tuple(deduplicate_categorizations(count2cat.values()))

        self._question = "What is the genotype group"
        self._hash = self._compute_hash()

    def _compute_hash(self) -> int:
        hash_value = 17

        self._groups = defaultdict(list)
        for count, cat in self._count2cat.items():
            hash_value += 13 * hash(count)
            hash_value += 13 * hash(cat)

        hash_value += 23 * hash(self._allele_counter)

        return hash_value

    def get_categorizations(self) -> typing.Sequence[Categorization]:
        return self._categorizations

    def get_question_base(self) -> str:
        return self._question

    def test(
        self,
        patient: Patient,
    ) -> typing.Optional[Categorization]:
        self._check_patient(patient)

        allele_count = self._allele_counter.count(patient)
        return self._count2cat.get(allele_count, None)

    def __eq__(self, value: object) -> bool:
        return (
            isinstance(value, ModeOfInheritancePredicate)
            and self._allele_counter == value._allele_counter
            and self._count2cat == value._count2cat
        )

    def __hash__(self) -> int:
        return self._hash

    def __str__(self) -> str:
        return (
            "ModeOfInheritancePredicate("
            f"allele_counter={self._allele_counter}, "
            f"count2cat={self._count2cat})"
        )

    def __repr__(self) -> str:
        return str(self)


class SexGenotypePredicate(GenotypePolyPredicate):
    # NOT PART OF THE PUBLIC API

    def __init__(self):
        self._categorizations = (
            Categorization(
                PatientCategory(
                    cat_id=0,
                    name="FEMALE",
                    description="Female",
                ),
            ),
            Categorization(
                PatientCategory(
                    cat_id=1,
                    name="MALE",
                    description="Male",
                ),
            ),
        )

    def get_categorizations(self) -> typing.Sequence[Categorization]:
        return self._categorizations

    def get_question_base(self) -> str:
        return "Sex of the individual"

    def test(self, patient: Patient) -> typing.Optional[Categorization]:
        if patient.sex.is_provided():
            if patient.sex.is_female():
                return self._categorizations[0]
            elif patient.sex.is_male():
                return self._categorizations[1]
            else:
                raise ValueError(f"Unsupported sex {patient.sex}")
        else:
            return None

    def __eq__(self, value: object) -> bool:
        return isinstance(value, SexGenotypePredicate)

    def __hash__(self) -> int:
        return 31


INSTANCE = SexGenotypePredicate()


def sex_predicate() -> GenotypePolyPredicate:
    """
    Get a genotype predicate for categorizing patients by their :class:`~gpsea.model.Sex`.

    See the :ref:`male-female-predicate` section for an example.
    """
    return INSTANCE


class DiagnosisPredicate(GenotypePolyPredicate):

    @staticmethod
    def create(
        diagnoses: typing.Iterable[typing.Union[str, hpotk.TermId]],
        labels: typing.Optional[typing.Iterable[str]] = None,
    ) -> "DiagnosisPredicate":
        # First, collect the iterables and check sanity.
        diagnosis_ids = []
        for d in diagnoses:
            if isinstance(d, str):
                d = hpotk.TermId.from_curie(d)
            elif isinstance(d, hpotk.TermId):
                pass
            else:
                raise ValueError(f"{d} is neither `str` nor `hpotk.TermId`")

            diagnosis_ids.append(d)

        if labels is None:
            labels = tuple(d.value for d in diagnosis_ids)
        else:
            labels = tuple(labels)

        assert (len(diagnosis_ids) >= 2), \
            f"We need at least 2 diagnoses: {len(diagnosis_ids)}"
        assert len(diagnosis_ids) == len(labels), \
            f"The number of labels must match the number of diagnose IDs: {len(diagnosis_ids)}!={len(labels)}"

        # Then, prepare the categorizations.
        categorizations = {
            diagnosis_id: Categorization.from_raw_parts(
                cat_id=i,
                name=diagnosis_id.value,
                description=label,
            )
            for i, (diagnosis_id, label) in enumerate(zip(diagnosis_ids, labels))
        }

        # Last, put the predicate together.
        return DiagnosisPredicate(categorizations)

    def __init__(
        self,
        categorizations: typing.Mapping[hpotk.TermId, Categorization],
    ):
        self._id2cat = dict(categorizations)
        self._categorizations = tuple(
            sorted(categorizations.values(), key=lambda c: c.category.cat_id)
        )
        self._hash = hash(tuple(categorizations.items()))

    def get_categorizations(self) -> typing.Sequence[Categorization]:
        return self._categorizations

    def get_question_base(self) -> str:
        return "What disease was diagnosed"

    def test(self, patient: Patient) -> typing.Optional[Categorization]:
        categorization = None
        for disease in patient.diseases:
            try:
                candidate = self._id2cat[disease.identifier]
            except KeyError:
                # No match for this disease, no problem.
                continue

            if categorization is None:
                # First time we found a candidate disease
                categorization = candidate
            else:
                # Ambiguous match. We found several matching diagnoses!
                return None

        return categorization
    
    def __eq__(self, value: object) -> bool:
        return isinstance(value, DiagnosisPredicate) \
            and self._id2cat == value._id2cat
    
    def __hash__(self) -> int:
        return self._hash


def diagnosis_predicate(
    diagnoses: typing.Iterable[typing.Union[str, hpotk.TermId]],
    labels: typing.Optional[typing.Iterable[str]] = None,
) -> GenotypePolyPredicate:
    """
    Create a genotype predicate that bins the patient based on presence of a disease diagnosis,
    as listed in :attr:`~gpsea.model.Patient.diseases` attribute.

    If an individual is diagnosed with more than one disease from the provided `diagnoses`,
    the individual will be assigned into no group (`None`).

    See the :ref:`diagnosis-predicate` section for an example.

    :param diagnoses: an iterable with at least 2 diagnose IDs, either as a `str` or a :class:`~hpotk.TermId`
      to determine the genotype group.
    :param labels: an iterable with diagnose names or `None` if CURIEs should be used instead.
      The number of labels must match the number of predicates.
    """
    return DiagnosisPredicate.create(
        diagnoses=diagnoses,
        labels=labels,
    )
