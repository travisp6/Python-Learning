provider "aws" {  
    region = "us-east-1"
}

resource "aws" "myserver" {
  ami = paste it from aws
  instance_type = "t2.micro"
   tags = {
       Name = someName
   }
}

resource "<provider>_<resource_type" "name" {
    config options.
    key = "value"
    key2 = "another value"
}

------------------------------------------------

use aws to create key pair (downloads folder)
# 1. Create VPC -google terraform aws vpc
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc

resource "aws_vpc" "myProject" {
  cidr_block = "10.0.0.0/16"
}

# 2. Create Internet Gateway -google terraform aws internet Gateway
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/internet_gateway

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id ## delete this and add from #1. \
         = aws_vpc.myProject.id
}

# 3. Create Custom Route Table -google terraform aws route table
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table
resource "aws_route_table" "example" {
  vpc_id = aws_vpc.example.id ##change from example to myProject

  route {
    cidr_block = "10.0.1.0/24" ## change to 0.0.0.0/0 to send all \
                               ## traffic to where it points
    gateway_id = aws_internet_gateway.example.id
  }

  route {
    ipv6_cidr_block        = "::/0"
    gateway_id = aws_egress_only_internet_gateway.example.id
  }

  tags = {
    Name = "example"
  }
}

# 4. Create A Subnet

resource "aws_subnet" "subnet-1" {
    vpc_id = aws_vpc.prod-vpc.id
    cidr_block = 10.0.1.0/24"
    availability_zone = "us-east-1a"
    
    tags = {
        Name = "prod-subnet"
    }
}

# 5. Associate subnet with Route Table -terraform aws route table association
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/route_table_association
#associates a subnet with a route table

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.example.id    ##change example to #4.example
  route_table_id = aws_route_table.example.id ##example to #3.example
}

# 6. Create Security Group to allow port
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group

resource "aws_security_group" "allow_web_traffic" {
  name        = "allow_web_traffic"
  description = "Allow web traffic"
  vpc_id      = aws_vpc.myProject.id

  ingress {
    description      = "HTTPS"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = [0.0.0.0/0]
    ipv6_cidr_blocks = ["::/0"]
  }
  ingress {
    description      = "SSH"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = [0.0.0.0/0]
    ipv6_cidr_blocks = ["::/0"]
  }
    ingress {
    description      = "HTTP"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = [0.0.0.0/0]
    ipv6_cidr_blocks = ["::/0"]
  }
  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1" ##-1 means any protocall
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_web"
  }
}

# 7. Create a network interface with an ip in the subnet that was created in step #4.
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/network_interface

resource "aws_network_interface" "test" {
  subnet_id       = aws_subnet.subnet-1.id ##from #4.
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.allow_web_traffic.id] ##from #6.

}

# 8. Assign an elastic IP to the network interface created in step #7.
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eip

resource "aws_eip" "one" {
  vpc                       = true
  network_interface         = aws_network_interface.test.id #from #7.
  associate_with_private_ip = "10.0.1.50"
  depends_on                = [aws_internet_gateway.gw] #must be a list []
}
##must have internet gateway

# 9. create aws server and install/enable apache2

resource "aws_instance" "web-server-instance" {
  ami = "ami-copypaste_from_aws"
  instance_type = "t2.micro"
  availability_zone = "us-east-1a"
  key_name = "example-key"

  network_interface {
    device_index = 0
    network_interface_id = aws_network_interface.test.id #from # 7.
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update -y
              sudo apt install apache2 -yes
              sudo systemctl start apache2
              sudo bash -c 'echo your very first web server > /var/www/html/index/html'
              EOF
  tags = {
    Name = "web-server"
  }
}