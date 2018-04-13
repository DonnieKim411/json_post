import json 
import hashlib
import base64
import urllib2
import requests
def calculate_MD5(filename):
	'''
	Calculate MD5 of an input file
	Input:
		filename: a filename in string
	output:
		MD5_hash: MD5 hash value in string
	'''
	hash_md5 = hashlib.md5()
	with open (filename, "rb") as f:
		for byte_chunk in iter(lambda: f.read(4096), b""):
			hash_md5.update(byte_chunk)

	return hash_md5.hexdigest()

def base64_encode(filename):
	with open(filename, "rb") as f:
		binary_data = f.read()
		encoded_file = base64.b64encode(binary_data)

	return encoded_file


# calculate MD5 cover letter, CV, and the script file
cover_letter_md5 = calculate_MD5('Arterys_Cover_Letter_Donnie_Kim.pdf')
resume_md5 = calculate_MD5('Resume_DonnieKIm.pdf')
code_md5 = calculate_MD5('json_creator.py')

# Base64 encode the files
cover_letter_base64 = str(base64_encode('Arterys_Cover_Letter_Donnie_Kim.pdf'))
resume_base64 = str(base64_encode('Resume_DonnieKIm.pdf'))
code_base64 = str(base64_encode('json_creator.py'))

# Fill out the json content
json_dict = {
    "email": "kdk411@gmail.com",
    "name": "Donnie Kim",
    "position": ["Machine Learning Scientist","Machine Learning Intern"],
    "notes": {
    	"GitHub repo": "https://github.com/kdk411",
    	"LinkedIn": "https://www.linkedin.com/in/donnie-kim-96a20490/"
    	},
    "phone": "(555) 664-7665",
    "documents": {
        "resume": {
            "content": resume_base64,
            "md5": resume_md5
        },
        "cover_letter": {
            "content": cover_letter_base64,
            "md5": cover_letter_md5
        },
        "code": {
            "content": code_base64,
            "md5": code_md5,
            "filename": "python_code_DonnieKim.tar.gz"
        }
    },
    "test_or_submit": "test"
}

dictionaryToJson_str = json.dumps(json_dict, sort_keys = True, indent=4)
#print(dictionaryToJson_str)

# # Write a json object
with open('json_object_DonnieKim.json', 'w') as out:
    json_object = json.dump(json_dict, out, indent = 4)

#post the json file
url = 'https://resumeapi.arterys.com/api/submission/3273a0ef-9253-4188-b728-197b2f802156'
req = requests.post(url, json = json_object)
print req.status_code

# i
# req = urllib2.Request(url)
# req.add_header('content_type', 'application/json')
# response = urllib2.urlopen(req, json_object)