#import io
from rest_framework import serializers
#from rest_framework.renderers import JSONRenderer
#from rest_framework.parsers import JSONParser
from .models import Women



#class WomenModel:
#    def __init__(self, title, content):
#        self.title = title
#       self.content = content





class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ("title", "content", "category")

#fields = "__all__"
#эта штука помогает сразу все поля вывести


"""
class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)
    
    def update(self, instance, validated_data):  #instance - сыылка на объект Women
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.save()
        return instance


        Короче здесь мы прописали вручную как происходит работа сериализатора.
        То есть как он использует данные для создания, просмотра и редактирования.
        В больших проектах может понадобиться свои сериализаторы
"""


"""
Получается, что сериализатор помогает условно кодировать и декодировать данные.
Сначала он берет наши объекты, тайтл, контент и тд, затем превращает в словар.
И потом он отдает их в виде JSON строки. Так же работает и в обратную сторону.

Получается как работает изменение записи. Оно делится на создание-create и обновление-update
То есть как сериализатор понимает, что хочет пользователь. 
Если мы просто хотим создать запись, данных в базе еще нет, и поэтому у нас всего один аргумент
Этот аргумент - validated_data. Потом сериализатор отрабатывает через представление.
Конкретно через метод post(view)
Если же мы хотим изменить запись, то сериализатор понимает
"""


#def encode():
#    model = WomenModel('Angelina', 'Content: Angelina Jolie')
#    model_sr = WomenSerializer(model)
#    print(model_sr.data, type(model_sr.data), sep='\n')
#    json = JSONRenderer().render(model_sr.data)
#    print(json)


#def decode():
#    stream = io.BytesIO(b'{"title":"Angelina","content":"Content: Angelina Jolie"}')
#    data = JSONParser().parse(stream)
#    serializer = WomenSerializer(data=data)
#    serializer.is_valid()
#    print(serializer.validated_data)

