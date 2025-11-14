import os 
import shutil
   
def copy(src,des):
    for item in os.listdir(src):
        src_path = os.path.join(src,item)
        print("FOUND:", src_path)
        if os.path.isfile(src_path):
            file_path = os.path.join(des,item)
            print("CREATING FILE:",file_path)
            shutil.copy(src_path,file_path)
        else: 
            dir_path = os.path.join(des,item)
            print("CREATING DIR:", dir_path)
            os.mkdir(dir_path)
            print("LOOKING FOR NESTED ITEMS TO COPY")
            copy(src_path,dir_path)

def copy_refresh(src,des):
    if os.path.exists(des):
        print("FOUND EXISTING DIR:", des)
        shutil.rmtree(des)
        print(f"{des} RESET")
    print("CREATING DIR:", des)
    os.mkdir(des)
    copy(src,des)            


