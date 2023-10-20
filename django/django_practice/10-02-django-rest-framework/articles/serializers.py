from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
      
        
class CommentSerializer(serializers.ModelSerializer):
    # 게시글의 제목만 가져오는 serializer 생성. 밖에 있었으면 가져다가 쓰는데 없으니까 class 안에서 새롭게 만듦
    class ArticleTitleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields = ('title',)
    # override
    # 덮어 씌우는 순간 CommentSerializer의 Meta에서 read_only_fields가 무효가 됨.
    # 모델 serializer가 read_only 기능 제공
    article = ArticleTitleSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',) # 유효성 검사에서 제외시키고, 데이터 조회 시에는 출력하는 기능

class ArticleSerializer(serializers.ModelSerializer):
    # 역참조 데이터 생성. related_name을 설정안해서 _set을 사용
    comment_set = CommentSerializer(many=True, read_only=True) # 여러 댓글이 달릴 수 있기 때문에, validation 피하기 위해
    # comment_count는 새로운 필드를 만드는 것이기 때문에 아무렇게나 이름 지어도 상관 없음. 
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        
        
