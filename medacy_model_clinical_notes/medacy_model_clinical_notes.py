import os

import spacy
from pkg_resources import resource_filename

from medacy.model.model import Model
from medacy.pipeline_components.feature_extractors.discrete_feature_extractor import FeatureExtractor
from medacy.pipeline_components.feature_overlayers.metamap.metamap_component import MetaMapOverlayer
from medacy.pipeline_components.learners.crf_learner import get_crf
from medacy.pipeline_components.tokenizers.systematic_review_tokenizer import SystematicReviewTokenizer
from medacy.pipelines.base.base_pipeline import BasePipeline


class N2C2Pipeline(BasePipeline):
    """
    Pipeline created for clinical notes; It was created for the extraction of ADE related entities
    from the 2018 N2C2 Shared Task.

    Created by Andriy Mulyar of NLP@VCU
    """

    def __init__(self, entities, **kwargs):
        super().__init__(entities, spacy_pipeline=spacy.load("en_core_web_sm"), **kwargs)

    def get_learner(self):
        return "CRF_l2sgd", get_crf()

    def get_tokenizer(self):
        return SystematicReviewTokenizer(self.spacy_pipeline)

    def get_feature_extractor(self):
        return FeatureExtractor(
            window_size=3,
            spacy_features=['pos_', 'shape_', 'prefix_', 'suffix_', 'text']
        )


def load():
    entities = ['Drug', 'Form', 'Route', 'ADE', 'Reason', 'Frequency', 'Duration', 'Dosage', 'Strength']
    pipeline = N2C2Pipeline(entities=entities)
    model = Model(pipeline, n_jobs=1)
    model_directory = resource_filename('medacy_model_clinical_notes', 'model')
    model.load(os.path.join(model_directory, 'n2c2_2020_jan_22.pkl'))
    return model
