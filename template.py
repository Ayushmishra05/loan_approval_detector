import os 

list_of_files = [
    f'.github/workflows/main.yaml', 
    f'data/', 
    f'models/', 
    f'src/', 
    f'src/__init__.py', 
    f'src/components/', 
    f'src/components/__init__.py', 
    f'src/pipeline/', 
    f'src/pipeline/__init__.py', 
    f'src/utils/', 
    f'src/utils/__init__.py', 
    f'src/utils/common/', 
    f'src/utils/common/__init__.py', 
    f'src/config/__init__.py', 
    f'src/utils/constants/', 
    f'src/utils/constants/__init__.py', 
    f"config/config.yaml", 
    f"./params.yaml", 
    f"./schema.yaml", 
    f"./main.py", 
    f"./Dockerfile", 
    f"./setup.py", 
    f"research/research.ipynb", 
    f"templates/index.html", 
    f"./app.py"


]

for file in list_of_files:
    dirname , filename = os.path.split(file) 
    os.makedirs(dirname , exist_ok= True)
    if len(filename) != 0:
        with open(file , 'w') as fp:
            pass 
    print(filename)