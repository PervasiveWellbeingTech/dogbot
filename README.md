# dog-voicebot
Voice-enabled dog chatbot for emotional therapy. 🐶

## Motivation
Traditional chatbots are all anthropomorphized. Even if a chatbot character is non-human, like a dog, robot or flower, the chatbot is still designed to respond in our preferred language. The exact dialog is written to convey its character's personality, but at the end of the day the chatbot is still communicating in a human way.

As a result, we expect chatbots to fulfill certain expectations of human communication. Specifically, we expect them to understand the content of what we're saying, and be able to respond appropriately. If a chatbot parses the content of our speech incorrectly, we become frustrated and disengage. This is even more apparent in chatbots designed for emotional therapy purposes. It's difficult for a chatbot to sound empathetic when it can't convey it understood what a user said.

But, what if a chatbot doesn't have to understand what a user says? People love dogs, and many dog-owners talk to their dog, wishing their pet could communicate to them. Yet, at no point do they expect the dog to understand what they're saying.

Despite lacking content understanding, dogs are still emotionally perceptive creatures. They respond to our emotions, barking and yipping at our excitement and whining when we're feeling down. This project aims to use this pattern of emotion-exclusive interaction to test a new modality through which to interface with chatbots.

Enter DogBot, an emotionally perceptive chatbot that is designed to respond with dog sounds that mirror the emotion in what you say. DogBot's goal is not to understand your problems and help you solve them, but to understand how you feel and validate those feelings. Hopefully, you feel better in the process.

### Dog+
Dog+ is an additional experiment to test if the addition of a small number of English words has an increased positive impact on participants, as opposed to using strictly dog sounds as responses.

## Dependencies

Note: You can use the environment.yml file to restore the conda environment for this project.

* Python 3.6
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [Pygame](https://www.pygame.org/wiki/GettingStarted) (for audio playback)

Currently using [Indico API](https://indico.io/docs) for emotion detection on the speech input transcript. Was using DeepAffects for analysis of the raw speech audio itself, but their models proved to be unreliable and error-prone.

Going forward, I seek to build custom emotion detection models optimized for this sort of conversational setting.


Developed by Cameron Cruz, under the direction of Pablo Paredes of the Pervasive Wellbeing Lab at Stanford University School of Medicine. Sponsored by Dan Jurafsky.
