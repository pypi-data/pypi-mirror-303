class Llama2Prompt:
    def __init__(self):
        self.user_start_token = "<s>[INST]"
        self.bot_start_token = "[/INST]"
        self.eos_token = "</s>"
        self.sys_prompt = (
            "<s>[INST] <<SYS>> You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. "
            "Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal data. "
            "Please ensure that your responses are socially unbiased and positive in nature. "
            "If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct."
            "If you don't know the answer to a question, please don't share false information.<</SYS>>"
        )

    def build_input(self, history=[], user_input=""):
        input_str = self.sys_prompt
        for idx, turn in enumerate(history):
            user_perfix = self.user_start_token if idx != 0 else ""
            bot_perfix = self.bot_start_token
            if turn["speaker"] == "user":
                input_str += user_perfix + turn["text"]
            else:
                input_str += bot_perfix + turn["text"] + self.eos_token
        user_perfix = self.user_start_token if len(history) != 0 else ""
        input_str += user_perfix + user_input + self.bot_start_token
        return input_str
    
    
class QWen2Prompt:
    def __init__(self):
        self.user_start_token = "<|im_start|>user\n"
        self.bot_start_token = "<|im_start|>assistant\n"
        self.eos_token = "<|im_end|>\n"
        self.sys_prompt = (
            "<|im_start|>system\nYou are a powerful and capable assistant who strictly follows user instructions and should make every effort to help users solve their problems.<|im_end|>\n"
        )

    def build_input(self, history=[], user_input=""):
        input_str = self.sys_prompt
        for idx, turn in enumerate(history):
            user_perfix = self.user_start_token
            bot_perfix = self.bot_start_token
            if turn["speaker"] == "user":
                input_str += user_perfix + turn["text"] + self.eos_token
            else:
                input_str += bot_perfix + turn["text"] + self.eos_token
        user_perfix = self.user_start_token
        input_str += user_perfix + user_input + self.eos_token + self.bot_start_token
        return input_str
    
    
    
    
class Llama3Prompt:
    def __init__(self):
        self.user_start_token = "<|start_header_id|>user<|end_header_id|>\n"
        self.bot_start_token = "<|start_header_id|>assistant<|end_header_id|>\n"
        self.eos_token = "<|eot_id|>"
        self.sys_prompt = (
            "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\nYou are a data synthesizer. Generating rewritten data that follow the format and content of the demo but include some variations to ensure the new data is diverse and realistic.\n<|eot_id|>"
        )

    def build_input(self, history=[], user_input=""):
        input_str = self.sys_prompt
        for idx, turn in enumerate(history):
            user_perfix = self.user_start_token
            bot_perfix = self.bot_start_token
            if turn["speaker"] == "user":
                input_str += user_perfix + turn["text"] + self.eos_token
            else:
                input_str += bot_perfix + turn["text"] + self.eos_token
        user_perfix = self.user_start_token
        input_str += user_perfix + user_input + self.eos_token + self.bot_start_token
        return input_str

    
    
class VicunaPsyPrompt:
    def __init__(self):
        self.user_start_token = "Client: "
        self.bot_start_token = "Counsellor: "
        self.eos_token = "</s>"
        self.sys_prompt = "you are the role of a professional counsellor who specialises in using a wide range of counselling techniques to provide deep guidance and insight. Avoid coaching responses and provide tailored advice to help the client based on the client's feedback."
        

    def build_input(self, history=[], user_input=""):
        input_str = self.sys_prompt
        for idx, turn in enumerate(history):
            user_perfix = self.user_start_token
            bot_perfix = self.bot_start_token
            if turn["speaker"] == "user":
                input_str += " " + user_perfix + turn["text"]
            else:
                input_str += " " + bot_perfix + turn["text"] + self.eos_token
        input_str += " " + self.user_start_token + user_input + " " +  self.bot_start_token
        return input_str



class MistralPrompt:
    def __init__(self):
        self.user_start_token = "[INST]"
        self.bot_start_token = "[/INST]"
        self.eos_token = "</s>"
        self.sys_prompt = (
            ""
        )

    def build_input(self, history=[], user_input=""):
        input_str = self.sys_prompt
        for idx, turn in enumerate(history):
            user_perfix = self.user_start_token
            bot_perfix = self.bot_start_token
            if turn["speaker"] == "user":
                input_str += user_perfix + turn["text"]
            else:
                input_str += bot_perfix + turn["text"] + self.eos_token
        input_str += self.user_start_token + user_input + self.bot_start_token
        return "<s>" + input_str



PROMPT_DICT = {
    "llama2": Llama2Prompt(), 
    "vicuna_psy": VicunaPsyPrompt(), 
    "mistral": MistralPrompt(), 
    "llama3": Llama3Prompt(),
    "qwen2": QWen2Prompt()
}
