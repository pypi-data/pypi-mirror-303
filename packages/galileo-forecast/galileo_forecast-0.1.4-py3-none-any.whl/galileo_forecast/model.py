# WIP

from pydantic import BaseModel, Field
from typing import Any, Dict, Type
import uuid
from numpy import ndarray
import lightgbm as lgb

class ModelInfo(BaseModel):
    base_model_class: Type[Any] = Field(default=None)
    submodel_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    submodel_object: Any
    predicted_probabilities: Dict[str, ndarray] = Field(default_factory=dict)
    performance_metrics: Dict[str, float] = Field(default_factory=dict)
    hyperparameters: Dict[str, Any] = Field(default_factory=dict)
    fitted: bool = Field(default=False)
    
    class Config:
        arbitrary_types_allowed = True

    def __post_init__(self):
        """
        Check if the base_model_class has a predict_proba method.
        """
        if not hasattr(self.base_model_class, 'predict_proba'):
            raise AttributeError("The submodel_object must have a 'predict_proba' method in order to use Thompson Sampling.")
        
        self.submodel_object = self.base_model_class(**self.hyperparameters)

    def __getitem__(self, key):
        return getattr(self, key)

    def get(self, key, default=None):
        return getattr(self, key, default)
    

def main():
    # Create a LightGBM model (not trained)
    lgb_model = lgb.LGBMClassifier(random_state=42)

    # Create a ModelInfo instance
    model_info = ModelInfo(
        base_model_class=lgb.LGBMClassifier,
        submodel_object=lgb_model,
        hyperparameters={'random_state': 42}
    )

    # Print results
    print(f"Submodel ID: {model_info.submodel_id}")
    print(f"Base Model Class: {model_info.base_model_class}")
    print(f"Hyperparameters: {model_info.hyperparameters}")
    print(f"Predicted Probabilities: {model_info.predicted_probabilities}")
    print(f"Performance Metrics: {model_info.performance_metrics}")

if __name__ == "__main__":
    main()




