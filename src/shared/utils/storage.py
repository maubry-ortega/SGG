import os
from supabase import create_client, Client
from fastapi import UploadFile, HTTPException
from src.core.config import settings
import uuid

class StorageService:
    def __init__(self):
        if not settings.SUPABASE_URL or not settings.SUPABASE_KEY:
             # In production, this should probably raise an error or warn. 
             # For development, we allow pass but methods will fail.
             self.client = None
             return

        self.client: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        self.bucket_name = "saggi-resources"

    async def upload_file(self, file: UploadFile, path_prefix: str = "pdfs") -> str:
        """
        Uploads a file to Supabase Storage and returns the public URL.
        """
        if not self.client:
            raise HTTPException(status_code=500, detail="Storage service not configured")

        file_content = await file.read()
        file_ext = file.filename.split(".")[-1]
        unique_filename = f"{uuid.uuid4()}.{file_ext}"
        file_path = f"{path_prefix}/{unique_filename}"

        try:
            # Upload file
            self.client.storage.from_(self.bucket_name).upload(
                file=file_content,
                path=file_path,
                file_options={"content-type": file.content_type}
            )
            
            # Get Public URL
            public_url = self.client.storage.from_(self.bucket_name).get_public_url(file_path)
            return public_url
        except Exception as e:
            print(f"Upload error: {e}")
            raise HTTPException(status_code=500, detail=f"Failed to upload file to storage: {str(e)}")

storage_service = StorageService()
