# portfolio-docker #

프로젝트용 테스트 홈페이지를 도커 컨테이너로 1 Instance로 운영하게 하는 테스트 git입니다.

[사용환경]

Amazon EC2의 t2.micro 인스턴스

Ubuntu 이미지 사용

git clone https://github.com/tryklab/portfolio-docker.git



[구동조건]

1. run_me.sh에 실행 권한 준 후 실행

2. sudo mount -t efs -o tls [AmazonEFS FS Address]:/ django # Amazon EFS 파일 시스템 마운트

3. sudo chown -R ubuntu:ubuntu django # 권한 변경

4. /djangoapp/config/settings.py 편집하여 RDS와 RedisCluster에 대한 설정값 기입하기(해당 부분 수정)
```
    DATABASES = {
        "default": {
            "ENGINE": 'django.db.backends.mysql',
            "NAME": '[DB Database Name]',
            "USER": '[DB USER Name]',
            "PASSWORD": '[DB PASSWORD]',
            "HOST": '[Master DB address]',
            "PORT": '3306',
        },
        'replica': {
            "ENGINE": 'django.db.backends.mysql',
            "NAME": '[DB Database Name]',
            "USER": '[DB USER Name]',
            "PASSWORD": '[DB PASSWORD]',
            "HOST": '[Replica DB address]',
            "PORT": '3306',
        },
    }
    CACHES = { 
        "default": { 
            "BACKEND": "django_redis.cache.RedisCache", 
            "LOCATION": [ 
                "redis://[Master RedisCache Server address]:6379", 
                "redis://[Secondary RedisCache Server address]:6379", ], 
            "OPTIONS": { 
                "CLIENT_CLASS": "django_redis.client.DefaultClient", 
                "MASTER_CACHE": "redis://[[Master RedisCache Server address]:6379", 
            }, 
        }
    }  
```
5. nginx/conf/nginx.conf 의 s3버킷 주소값을 수정한다.
```
    location ~^/static/(.+)$ {
        resolver [VPC CIDR, last .2]; # VPC CIDR값에서 끝자리가 2인것으로 기입한다. ex) CIDR = 10.0.0.0/16 -> 10.0.0.2
        proxy_pass https://[bucket_address]/$1;
    }
```

5. djangoapp 폴더에서 마운팅된 django 폴더로 내용 복사 # cp -R * ../django

6. Plz_move_me_s3bucket 내용물 s3 버킷으로 업로드

7. portainer 폴더에서 sudo docker-compose up -d # 필요없을경우 생략

8. sudo docker build -t django:v2 . # 장고 서비스용 컨테이너 빌드

9. sudo docker-compose up -d

10. django 컨테이너 접속 후
``` 
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
```
11. /etc/fstab 파일 수정
```
    [AmazonEFS FS Address]:/  [django폴더 절대경로]     efs    _netdev,tls       0   0
```
