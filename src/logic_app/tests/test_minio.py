# from __future__ import annotations
# import os
# import sys
# import unittest
# from pathlib import Path
# from minio.error import S3Error
# from PIL import Image  # Library to create an image file
# from shared.minio import MinioClient
# from shared.minio import MinIOInput
# sys.path.append(str(Path(__file__).parent.parent))
# class TestMinioClient(unittest.TestCase):
#     """Test case class for MinioClient functionality."""
#     def setUp(self):
#         """Set up the test environment before each test case.
#         Initializes MinioClient, creates a test image, and prepares a bucket.
#         """
#         # Initialize MinioClient instance
#         self.client = MinioClient()
#         self.bucket_name = 'test-bucket'  # Name of the test bucket
#         self.object_name = 'test_image.png'  # Name of the test image object in MinIO
#         self.local_file = r'tests\test_db\test_image.png'  # Path to the local test image
#         # Path to the downloaded image
#         self.download_file = r'tests\test_db\downloaded_test_image.png'
#         # Create 'local' directory if it doesn't exist
#         os.makedirs('test_db', exist_ok=True)
#         # Create a test image (100x100 red square)
#         img = Image.new('RGB', (100, 100), color='red')
#         img.save(self.local_file, 'PNG')
#         # Store original file size for comparison
#         self.original_size = os.path.getsize(self.local_file)
#         # Create test bucket if it doesn't exist
#         try:
#             if not self.client.minio_client.bucket_exists(self.bucket_name):
#                 self.client.minio_client.make_bucket(self.bucket_name)
#         except S3Error as e:
#             self.fail(f'Failed to create bucket in setUp: {e}')
#     def tearDown(self):
#         """Clean up after each test case.
#         Removes local files, deletes the object from MinIO, and removes the bucket if empty.
#         """
#         # Remove local files if they exist
#         if os.path.exists(self.local_file):
#             os.remove(self.local_file)
#         if os.path.exists(self.download_file):
#             os.remove(self.download_file)
#         # Delete object from MinIO bucket
#         try:
#             self.client.minio_client.remove_object(
#                 self.bucket_name, self.object_name,
#             )
#         except S3Error:
#             pass  # Ignore if object doesn't exist
#         # Remove bucket if it's empty
#         try:
#             self.client.minio_client.remove_bucket(self.bucket_name)
#         except S3Error:
#             pass  # Ignore if bucket is not empty or doesn't exist
#     def test_put_object(self):
#         """Test uploading an image file to MinIO.
#         Verifies that the upload operation succeeds and the object name matches.
#         """
#         # Prepare input data for upload
#         input_data = MinIOInput(
#             bucket_name=self.bucket_name,
#             object_name=self.object_name,
#             file_path=self.local_file,
#         )
#         # Execute upload operation
#         future = self.client.put_object(input_data)
#         result = future.result(timeout=5)
#         # Assert upload was successful and object name is correct
#         self.assertIsNotNone(result, 'Upload failed: Result is None')
#         self.assertEqual(
#             result.object_name, self.object_name,
#             'Object name does not match',
#         )
#     def test_get_object(self):
#         """Test downloading an image file from MinIO.
#         Uploads an image first, then downloads it and verifies the file exists and matches the original size.
#         """
#         # Upload the image first
#         upload_input = MinIOInput(
#             bucket_name=self.bucket_name,
#             object_name=self.object_name,
#             file_path=self.local_file,
#         )
#         self.client.put_object(upload_input).result(timeout=5)
#         # Prepare input data for download
#         download_input = MinIOInput(
#             bucket_name=self.bucket_name,
#             object_name=self.object_name,
#             file_path=self.download_file,
#         )
#         # Execute download operation
#         future = self.client.get_object(download_input)
#         result = future.result(timeout=5)
#         # Assert download was successful and file exists
#         self.assertIsNotNone(result, 'Download failed: Result is None')
#         self.assertTrue(
#             os.path.exists(self.download_file),
#             'Downloaded file does not exist',
#         )
#         # Verify downloaded file size matches the original
#         downloaded_size = os.path.getsize(self.download_file)
#         self.assertEqual(
#             downloaded_size, self.original_size,
#             'Downloaded file size does not match original',
#         )
#     def test_delete_object(self):
#         """Test deleting an image file from MinIO.
#         Uploads an image first, deletes it, and verifies it no longer exists.
#         """
#         # Upload the image first
#         upload_input = MinIOInput(
#             bucket_name=self.bucket_name,
#             object_name=self.object_name,
#             file_path=self.local_file,
#         )
#         self.client.put_object(upload_input).result(timeout=5)
#         # Prepare input data for deletion
#         delete_input = MinIOInput(
#             bucket_name=self.bucket_name,
#             object_name=self.object_name,
#         )
#         # Execute delete operation
#         self.client.delete_object(delete_input)
#         # Verify object has been deleted by expecting a NoSuchKey error
#         with self.assertRaises(S3Error) as context:
#             self.client.minio_client.stat_object(
#                 self.bucket_name, self.object_name,
#             )
#         self.assertIn(
#             'NoSuchKey', str(context.exception),
#             'Object was not deleted',
#         )
#     def test_list_buckets(self):
#         """Test listing buckets in MinIO.
#         Verifies that the test bucket is included in the list of buckets.
#         """
#         # Get list of buckets
#         buckets = self.client.list_buckets()
#         # Assert listing was successful and test bucket exists
#         self.assertIsNotNone(buckets, 'List buckets failed')
#         self.assertTrue(
#             any(b.name == self.bucket_name for b in buckets),
#             f'Bucket {self.bucket_name} not found',
#         )
# if __name__ == '__main__':
#     unittest.main()
from __future__ import annotations
