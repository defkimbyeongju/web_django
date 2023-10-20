import json
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer, TopicSerializer
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Article, Topic
# Create your views here.
# serializer는 데이터를 json 형태로 변환하는 역할.

@api_view(['GET','POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        # 쿼리셋을 json 형태로 포장    
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        # print(request.data.get('topics')) # 리스트가 아닌 문자열 데이터 타입
        topics_string = request.data.get('topics')
        topics_data = json.loads(topics_string)
        
        # topics_data 반복하면서
        # 1. Topic 테이블에 새로운 토픽이라면 추가
        # 2. 기존에 있다면, 저장은 하지 않음
        # 3. 기존에 있던 없던 생성하려던 게시글과는 관계를 설정해줘야 한다.
        
        # 비어 있는 리스트
        topics = []
        # topics_data: 리스트
        # topic: 문자열
        for topic in topics_data:
            # 토픽 데이터를 딕셔너리로 정의
            topic_data = {"name":topic}
            topic_serializer = TopicSerializer(data=topic_data)
            # 존재하면 exist_topic 변수에 담김
            exist_topic = Topic.objects.filter(name=topic).first()
            if exist_topic:
                # 관계 설정을 위해 비어있는 리스트에 추가
                topics.append(exist_topic)
            else:
                # 없다면 생성
                if topic_serializer.is_valid(raise_exception=True):
                    topic_serializer.save()
                    # 생성한 인스턴스를 리스트에 추가
                    topics.append(topic_serializer.instance)
                    
        serializer = ArticleListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): # raise_exception: Valid 하지 못했을 때, error문을 돌려주는 기능
            article = serializer.save()
            
            # article - topics 관계 설정
            # set: 여러 개의 데이터를 한 번에 관계 지어줌
            article.topics.set(topics)
            
            # 이렇게만 적으면 조회랑 구별 x
            # 그래서, status를 사용
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET','DELETE', 'PUT'])
def article_detail(request, article_pk):
    # 없는 데이터를 조회하면 버그 발생
    # article = Article.objects.get(pk=article_pk)
    
    # 버그가 아닌, 에러 상태를 잘 돌려줘야 한다.
    article = get_object_or_404(Article, pk=article_pk)
    
    # GET 요청 들어올 때 마다 views 필드 값을 +1 하는 방법
    if request.method == "GET":
        # 조회수 추가. save를 해줘야 DB에 저장됨
        article.views += 1
        article.save()
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # 삭제 메시지를 주고 싶다면 아래와 같이 작성
        # return Response({'message': "삭제 완료"}, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        # partial = True : 수정 시 특정 필드만 입력받고 싶을 때
        serializer = ArticleSerializer(article, data=request.data, partial=True) # 해당 article을 받은 data로 바꿔라.
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        