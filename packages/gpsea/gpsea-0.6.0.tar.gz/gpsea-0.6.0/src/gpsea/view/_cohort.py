import typing

from hpotk import MinimalOntology
from jinja2 import Environment, PackageLoader
from collections import namedtuple

from gpsea.model import Cohort
from ._report import GpseaReport, HtmlGpseaReport
from ._formatter import VariantFormatter


ToDisplay = namedtuple('ToDisplay', ['hgvs_cdna', 'hgvsp', 'variant_effects'])


class CohortViewer:
    """
    `CohortViewer` summarizes the most salient :class:`~gpsea.model.Cohort` aspects into an HTML report.
    """

    def __init__(
            self,
            hpo: MinimalOntology,
            top_phenotype_count: int = 10,
            top_variant_count: int = 10,
    ):
        """
        Args:
            hpo(MinimalOntology): An HPO ontology object from hpo-toolkit
            top_phenotype_count(int): Maximum number of HPO terms to display in the HTML table (default: 10)
            top_variant_count(int): Maximum number of variants to display in the HTML table (default: 10)
        """
        self._hpo = hpo
        self._top_phenotype_count = top_phenotype_count
        self._top_variant_count = top_variant_count
        environment = Environment(loader=PackageLoader('gpsea.view', 'templates'))
        self._cohort_template = environment.get_template("cohort.html")

    def process(
        self,
        cohort: Cohort,
        transcript_id: typing.Optional[str] = None,
    ) -> GpseaReport:
        """
        Generate the report for a given `cohort`.

        Args:
            cohort (Cohort): The cohort being analyzed in the current Notebook
            transcript_id (str): the transcript that we map variants onto

        Returns:
            GpseaReport: a report that can be stored to a path or displayed in
                interactive environment such as Jupyter notebook.
        """
        context = self._prepare_context(cohort, transcript_id=transcript_id)
        report = self._cohort_template.render(context)
        return HtmlGpseaReport(html=report)

    def _prepare_context(
        self,
        cohort: Cohort,
        transcript_id: typing.Optional[str],
    ) -> typing.Mapping[str, typing.Any]:

        hpo_counts = list()
        for hpo in cohort.list_present_phenotypes(top=self._top_phenotype_count):
            hpo_id = hpo[0]
            individual_count = hpo[1]
            hpo_label = "n/a"
            if hpo_id in self._hpo:
                hpo_label = self._hpo.get_term_name(hpo_id)
            hpo_counts.append(
                {
                    "HPO": hpo_label,
                    "ID": hpo_id,
                    "Count": individual_count,
                }
            )

        variant_counts = list()
        variant_to_display_d = CohortViewer._get_variant_description(cohort, transcript_id)
        for variant_key, count in cohort.list_all_variants(top=self._top_variant_count):
            # get HGVS or human readable variant
            if variant_key in variant_to_display_d:
                display = variant_to_display_d[variant_key]
                hgvs_cdna = display.hgvs_cdna
                protein_name = display.hgvsp
                effects = '' if display.variant_effects is None else ", ".join(display.variant_effects)
            else:
                display = variant_key
                hgvs_cdna = ''
                protein_name = ''
                effects = ''

            variant_counts.append(
                {
                    "variant": variant_key,
                    "variant_name": hgvs_cdna,
                    "protein_name": protein_name,
                    "variant_effects": effects,
                    "Count": count,
                }
            )

        disease_counts = list()
        for disease_id, disease_count in cohort.list_all_diseases():
            disease_name = "Unknown"
            for disease in cohort.all_diseases():
                if disease.identifier == disease_id:
                    disease_name = disease.name
            disease_counts.append(
                {
                    "disease_id": disease_id,
                    "disease_name": disease_name,
                    "count": disease_count,
                }
            )

        n_diseases = len(disease_counts)

        var_effects_list = list()
        var_effects_d = dict()
        if transcript_id is not None:
            has_transcript = True
            data_by_tx = cohort.variant_effect_count_by_tx(tx_id=transcript_id)
            # e.g., data structure
            #   -- {'effect}': 'FRAMESHIFT_VARIANT', 'count': 175},
            #   -- {'effect}': 'STOP_GAINED', 'count': 67},
            for tx_id, counter in data_by_tx.items():
                if tx_id == transcript_id:
                    for effect, count in counter.items():
                        var_effects_d[effect] = count
            total = sum(var_effects_d.values())
            # Sort in descending order based on counts
            sorted_counts_desc = dict(sorted(var_effects_d.items(), key=lambda item: item[1], reverse=True))
            for effect, count in sorted_counts_desc.items():
                percent = f"{round(count / total * 100)}%"
                var_effects_list.append({"effect": effect, "count": count, "percent": percent})
        else:
            has_transcript = False
            transcript_id = "MANE transcript ID"
            
        # The following dictionary is used by the Jinja2 HTML template
        return {
            "n_individuals": len(cohort.all_patients),
            "n_excluded": cohort.get_excluded_count(),
            "total_hpo_count": len(cohort.all_phenotypes()),
            "top_hpo_count": self._top_phenotype_count,
            "hpo_counts": hpo_counts,
            "unique_variant_count": len(cohort.all_variants()),
            "top_var_count": self._top_variant_count,
            "var_counts": variant_counts,
            "n_diseases": n_diseases,
            "disease_counts": disease_counts,
            "has_transcript": has_transcript,
            "var_effects_list": var_effects_list,
            "transcript_id": transcript_id,
        }

    @staticmethod
    def _get_variant_description(
        cohort: Cohort,
        transcript_id: typing.Optional[str],
        only_hgvs: bool = True,
    ) -> typing.Mapping[str, ToDisplay]:
        """
        Get user-friendly strings (e.g., HGVS for our target transcript) to match to the chromosomal strings
        Args:
            cohort (Cohort): The cohort being analyzed in the current Notebook
            transcript_id (str): the transcript that we map variants onto
            only_hgvs (bool): do not show the transcript ID part of the HGVS annotation, just the annotation.

        Returns:
            typing.Mapping[str, ToDisplay]:
              key: variant key,
              value: namedtuple(display (e.g. HGVS) string of variant, hgvsp protein string of variant)
        """
        chrom_to_display = dict()
        var_formatter = VariantFormatter(transcript_id)

        for var in cohort.all_variants():
            variant_key = var.variant_info.variant_key
            display = var_formatter.format_as_string(var)
            if transcript_id is None:
                tx_annotation = None
            else:
                tx_annotation = var.get_tx_anno_by_tx_id(transcript_id)
            
            if tx_annotation is None:
                hgvsp = None
                var_effects = None
            else:
                hgvsp = tx_annotation.hgvsp
                var_effects = [var_eff.name for var_eff in tx_annotation.variant_effects]
    
            if only_hgvs:
                # do not show the transcript id
                fields_dna = display.split(":")
                fields_ps = hgvsp.split(":") if hgvsp is not None else [None]
                if len(fields_dna) > 1:
                    display = fields_dna[1]
                else:
                    display = fields_dna[0]
                if len(fields_ps) > 1:
                    hgvsp = fields_ps[1]
                else:
                    hgvsp = fields_ps[0]
            chrom_to_display[variant_key] = ToDisplay(display, hgvsp, var_effects)

        return chrom_to_display
