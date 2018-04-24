from graphene_django import DjangoObjectType
import graphene
from .models import Note as NoteModel


class Note(DjangoObjectType):
  class Meta:
    model = NoteModel
    interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
  notes = graphene.List(Note)

  def resolve_notes(self, info):
    user = info.context.user
    if user.is_anonymous:
      return NoteModel.objects.none()
    else:
      return NoteModel.objects.filter(user=user)


schema = graphene.Schema(query=Query)
