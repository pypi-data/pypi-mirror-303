from openagi.llms.azure import AzureChatOpenAIModel
from openagi.agent import Admin
from openagi.memory import Memory
from openagi.worker import Worker
from openagi.planner.task_decomposer import TaskPlanner
from openagi.actions.base import BaseAction

import wikipedia
import os
import joblib
import requests
import re
import string
from tqdm import tqdm
from collections import Counter
from pydantic import Field, field_validator
import numpy as np

class WikiSearchAction(BaseAction):
  """
  Use this Action to get the information from Wikipedia Search
  """
  query: str = Field(
      default_factory=str,
      description="The search string. be simple"
    )

  def execute(self):
    search_res = wikipedia.search(self.query)
    if not search_res:
      return 'No results found.'
    article = wikipedia.page(search_res[0])
    return article.summary

def download_file(url, filename):
    """
    Download a file from a URL and save it locally.
    """
    response = requests.get(url)
    response.raise_for_status()
    with open(filename, "wb") as f:
        f.write(response.content)
    print(f"Downloaded {filename}")


def load_hotpot_qa_data(level):
    """
    Load HotpotQA data for a given level. If data doesn't exist, download it.
    """
    file_path = f"./data/{level}.joblib"
    data_url = (
        f"https://github.com/salesforce/BOLAA/raw/main/hotpotqa_run/data/{level}.joblib"
    )

    if not os.path.exists(file_path):
        print(f"{level} data not found, downloading...")
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        download_file(data_url, file_path)
    # joblib requires python 3.10 or higher
    return joblib.load(file_path)

def normalize_answer(s):
    """
    Normalize answers for evaluation.
    """

    def remove_articles(text):
        return re.sub(r"\b(a|an|the)\b", " ", text)

    def white_space_fix(text):
        return " ".join(text.split())

    def remove_punc(text):
        exclude = set(string.punctuation)
        return "".join(ch for ch in text if ch not in exclude)

    def lower(text):
        return text.lower()

    return white_space_fix(remove_articles(remove_punc(lower(s))))


def f1_score(prediction, ground_truth):
    """
    Compute the F1 score between prediction and ground truth answers.
    """
    prediction_tokens = normalize_answer(prediction).split()
    ground_truth_tokens = normalize_answer(ground_truth).split()
    common = Counter(prediction_tokens) & Counter(ground_truth_tokens)
    num_same = sum(common.values())
    if num_same == 0:
        return 0, 0, 0
    precision = 1.0 * num_same / len(prediction_tokens)
    recall = 1.0 * num_same / len(ground_truth_tokens)
    f1 = (2 * precision * recall) / (precision + recall)
    return f1, precision, recall

def agent(query , llm):
    planner = TaskPlanner(autonomous=True)
    # for autonomous = False
    """
    planner = TaskPlanner(autonomous=False,human_intervene=False)
    
    researcher = Worker(
        role="Wikipedia Researcher",
        instructions="You are an intelligent Wikipedia agent. Your generation should follow the example format. Finish the task if you find the answer. And you answer should be simple and straighforward. DO NOT repeat your actions.",
        actions=[WikiSearchAction],
        max_iterations = 3,
    )"""
    admin = Admin(
        planner=planner,
        memory=Memory(),
        actions=[WikiSearchAction],
        llm=llm,
    )
    # admin.assign_workers([researcher]) #un-comment this for Autonomous = False

    res = admin.run(
        query=query,
        description="Provide answer for the query.You should decompose your task into executable actions.",
    )
    return res

def run_agent(level = 'easy'):
    os.environ["AZURE_BASE_URL"] = ""
    os.environ["AZURE_DEPLOYMENT_NAME"] = ""
    os.environ["AZURE_MODEL_NAME"]="gpt4"
    os.environ["AZURE_OPENAI_API_VERSION"]=""
    os.environ["AZURE_OPENAI_API_KEY"]=  ""
    config = AzureChatOpenAIModel.load_from_env_config()
    llm = AzureChatOpenAIModel(config=config)

    hotpot_data = load_hotpot_qa_data(level)
    hotpot_data = hotpot_data.reset_index(drop=True)
    task_instructions = [
        (row["question"], row["answer"]) for _, row in hotpot_data.iterrows()
    ]

    f1_list = []
    correct = 0
    results = {}

    for task , answer in tqdm(task_instructions[0:30]):
        response = agent(task , llm)
        f1 , _ ,_ = f1_score(response,answer)
        f1_list.append(f1)
        correct += int(response == answer)

        avg_f1 = np.mean(f1_list)
        acc = correct / len(task_instructions[0:30])
    return avg_f1, acc

# levels are 'easy' , 'medium' , 'hard'
f1 , acc = run_agent(level='easy')
print(f"F1 score : {f1} , Accuracy : {acc}")