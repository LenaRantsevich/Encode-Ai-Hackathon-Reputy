#import the dependencies
import openai
from openai import OpenAI
import tempfile
import os
import json
import time


 #Specify the path to your local JSON file

file_path = 'instagram\instagram_data.json'
client = OpenAI(api_key= os.environ.get("OPENAI_API_KEY"))

def open_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def open_txtfile(file_path):
    with open(file_path, 'r', encoding='utf-8') as infile:
        return infile.read().strip()

#get the data from the instagram
instagram_data= open_file(file_path)
data_section = instagram_data['data']

#Funtion to get url with ID
def get_url(data_section,target_id):
    for item in data_section:
        if item['id'] == target_id:
            return item['media_url']
    return "URL not found"

#Function to get captions with id
def get_captions(data_section,target_id):
    for item in data_section:
        if item['id'] == target_id:
            return item['caption']
    return "URL not found"


# Extracting IDs and captions and saving them to a list of tuples
id_caption_list = [(item['id'], item['caption']) for item in data_section]

with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.json', encoding='utf-8') as temp_file:
    data_section_str = json.dumps(id_caption_list, indent=4) 
    
    # Write the JSON data to the temporary file
    temp_file.write(data_section_str)
    # Store the path to the temporary file for later use
    temp_filepath = temp_file.name

    
with open(temp_filepath,'rb') as file_data:
    uploaded_file= client.files.create(file=file_data,purpose="assistants")
captions = '\n'.join([f"ID: {item['id']}, Caption: \"{item['caption']}\"" for item in data_section])
skills = ["Problem-Solving", "Ability to learn fast", "Communication", "Collaboration", "Attention to Detail", "Time Management"]
prompt = f"Given the following captions, identify which relate to these skills: {', '.join(skills)}. For each skill, list the ID(s) from the captions that best represent the skill. Format your response as 'Skill: [ID(s)]'. If a caption does not relate to any of the skills, omit it.\n\n{captions}"
assistant=client.beta.assistants.create(
    name="Skill set analyser",
    instructions= prompt,
    model ="gpt-4-1106-preview",
    tools=[
        {"type":"retrieval"}],
    file_ids=[uploaded_file.id]

)

#Create a thread
thread=client.beta.threads.create()

#add a user message to the thread
user_input= "SELECT ONLY 3 MOST REPRESENTED SKILLS TO OUTPUT. Format your response as {'Skill': 'ID(s)'}.If there are more than one id matching to a skill. format the skill twice with ID for eg {'skill 1':'ID 1', 'skill 2': 'ID 2} OUTPUT NOTHING OTHER THAN THE GIVE OUTPUT FORMAT"
message=client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_input
)    
# Start a run of the assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id
)

#wait for the run to complete and then retrieve messages
while True:
    run_status = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id= run.id
    )
    if run_status.status == 'completed':
        break
    time.sleep(0.01)


folder_path = 'output.txt'  # Replace this with the actual path

# Construct the full path to the file within the specified folder
file_path = os.path.join(folder_path, 'output.txt')

# Open the file at the specified path in write mode
for message in client.beta.threads.messages.list(thread_id=thread.id):
        if message.role == 'assistant':
            final_out=message.content[0].text.value
            final_out_dict = json.loads(final_out.replace("'", '"'))
            print(final_out)

collected_data=[]
for key,value in final_out_dict.items():
    skill= key
    caption= get_captions(data_section=data_section,target_id=value)
    media= get_url(data_section=data_section,target_id=value)
    collected_data.append({"skill": skill, "caption": caption, "media_url": media})

# Write the collected data to a JSON file
with open('output_file.json', 'w') as f:
    json.dump(collected_data, f, indent=4)

print("Data has been written to output_file.json")




        
# Clean up: REMOVE THE TEMPORARY FILE AFTER UPLOADING
os.remove(temp_filepath)
