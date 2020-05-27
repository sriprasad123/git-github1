import boto3
import os

BUCKET= 'thumbnail111'

#Listing all the objects in the bucket:
def list():
    s3_list = boto3.resource('s3')
    list = s3_list.Bucket(BUCKET)
    print("Objects in the bucket: \n")
    for key in list.objects.all():
        print(key.key)
    return main()

#upload the files to S3:
s3_upload = boto3.client('s3')
s3_upload_folder = boto3.resource('s3')
def upload():
    source_file = input("\nplease provide fully qualified source filename: \n")
    file_reader = open(source_file).read()
    base_file = os.path.basename(source_file)
    command1 = input("\nSpecify the folder to upload the file Models/Artifacts\n")
    if (command1 == 'Models'):
        #upload to Models folder
        s3_upload_folder.Bucket(BUCKET).upload_file(source_file, '%s/%s' % ('Models', base_file))
    elif (command1 == 'Artifacts'):
        # upload to Artifacts folder
        s3_upload_folder.Bucket(BUCKET).upload_file(source_file, '%s/%s' % ('Artifacts', base_file))
    else:
        # upload to bucket
        s3_upload.put_object(
        ACL = 'private',
        Body = file_reader,
        Bucket = BUCKET,
        Key = base_file)
    print("Object uploaded successfully!!")
    return main()

# Download the files from S3:
def download():
    dest_path = input("please provide the path to store the file: \n")
    folder= input("Specify the folder to download the file Models/Artifacts\n")
    file = input("Please specify the name of the file to be downloaded:\n")
    s3 = boto3.client('s3')
    s3.download_file(BUCKET, ( folder +'/'+ file),dest_path+'/'+ file)
    print("Object downloaded successfully!!")
    return main()

def main():
    action = input("\nSpecify your action as upload/download/list \n")
    if action == "upload":
        upload()
    elif action == "download":
        download()
    elif action == "list":
        list()
    else:
        command = input("Something went wrong, do you wish to continue? yes/no\n")
        if command == ('yes'):
            return main()
        elif command == ('no'):
            print("Thank you!!")

if __name__ == '__main__':
    main()