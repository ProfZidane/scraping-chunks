import os
import json


def save_on_disk(chunks, output_dir="scraped_chunks"):
    os.makedirs(output_dir, exist_ok=True)
    for i, chunk in enumerate(chunks):
        with open(f"{output_dir}/chunk_{i}.json", "w") as f:
            json.dump({"content": chunk}, f)

    print(f"Documents découpés et sauvegardés dans {output_dir}")


# if necessary push on bucket GCP
""" from google.cloud import storage
import glob
def upload_to_gcs(bucket_name, source_folder):
    client = storage.Client()
    bucket = client.bucket(bucket_name)

    for file_path in glob.glob(f"{source_folder}/*.json"):
        blob = bucket.blob(os.path.basename(file_path))
        blob.upload_from_filename(file_path)
        print(f"Uploaded {file_path} to GCS bucket {bucket_name}") """