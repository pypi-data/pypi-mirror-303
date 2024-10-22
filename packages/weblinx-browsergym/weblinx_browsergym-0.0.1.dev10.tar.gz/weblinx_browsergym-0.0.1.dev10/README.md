# agentlab-weblinx-mvp

MVP version of agentlab-weblinx, we will either merge as fork/PR or create a public repo at release

## Running experiments

If you just want to run experiments, you should be able to simply run the following code:

```bash
# export HF_TOKEN to be your huggingface token
# note: you need to request access to the dataset
export HF_TOKEN="<your_huggingface_token>"

# install agentlab fork
git clone https://github.com/xhluca/AgentLab
cd AgentLab/

# optional: create a virtual environment
python -m venv venv && source venv/bin/activate

# install agentlab
pip install -e .

# now, you can run the agent
cd ../
pip install weblinx-browsergym
git clone https://github.com/McGill-NLP/agentlab-weblinx-mvp
python agentlab-weblinx-mvp/run_agent.py
```

## Install agentlab

Install the agentlab package:

```bash
git clone https://github.com/xhluca/AgentLab
cd AgentLab/
pip install -e .
```

Then, you can run the following code to test the environment:

```python
import weblinx_browsergym

# pattern: weblinx.<demo_id>.<step>
tasks = weblinx_browsergym.list_tasks(split=split, metadata_path="./metadata.json")
env = weblinx_browsergym.make(f"browsergym/{tasks[100]}")
obs, info = env.reset()
action = 'click(bid="baf79046-bd85-4867")'
obs, reward, done, info = env.step(action)

assert done is True, "Episode should end after one step"
assert 0 <= reward <= 1, "Reward should be between 0 and 1"
```

If you want to register tasks, you can run the following code:

```python
# register tasks at import
import weblinx_browsergym.tasks
```

Or do it manually with:

```python
# register tasks manually
from weblinx_browsergym import register_weblinx_tasks

register_weblinx_tasks()
```

# Data processing

All in one:

```bash
pip install -r requirements.txt

# get snapshots
playwright install
python processing/get_snapshots.py

# create metadata.json
python processing/create_metadata_json.py

# prepare data for agentlab
python processing/prepare_data_for_agentlab.py

# upload to huggingface
huggingface-cli upload-large-folder McGill-NLP/weblinx-browsergym ./bg_wl_data --repo-type=dataset
```

## 1. Get snapshots (dom object, axtree, extra properties)

To get snapshots, you need to first install `playwright`:

```bash
pip install -r requirements.txt
playwright install
```

Then, you can run the following code to get snapshots:

```bash
python processing/get_snapshots.py
```

## 2. Create a `metadata.json` file

To create a `metadata.json` file, run the following code:

```bash
python processing/create_metadata_json.py
```

## 3. Update set-of-marks inside the demos

To update the set-of-marks inside the demos, run the following code:

```bash
python processing/update_set_of_marks.py
```

## 4. Copy, zip demos into `bg_wl_data` folder and upload

We store a copy of the full data in the `bg_wl_data` folder, followed by creating zips. To copy the files, run the following code:

```bash
python processing/prepare_data_for_agentlab.py
```

You can upload this `bg_wl_data` folder to huggingface hub with:

```bash
huggingface-cli upload-large-folder McGill-NLP/weblinx-browsergym ./bg_wl_data --repo-type=dataset
```

# Run agent

To run the agent, you can use the following code:

```bash
# optional: set directory where the cache is stored
export BROWSERGYM_WEBLINX_CACHE_DIR="./bg_wl_data"
python run_agent.py
```

# Build and release python package

To build and release the python package, you can run the following code:

```bash
pip install twine wheel

# Delete existing dist/ folder and build the package
rm -r dist/ && python setup.py sdist bdist_wheel

# Then, upload to pypi
twine upload dist/* --repository weblinx-browsergym
```