from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.components import ComponentBuilder
from rasa_nlu.model import Trainer

builder = ComponentBuilder(use_cache=True)

training_data = load_data("./nlu.md")
trainer = Trainer(config.load("./nlu_config.yml"), builder)
trainer.train(training_data)
model_directory = trainer.persist("./models")