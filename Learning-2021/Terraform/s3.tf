resource "aws_s3_bucket" "b" {
  bucket = "rl-s3-bucket"
  acl    = "public-read-write"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}