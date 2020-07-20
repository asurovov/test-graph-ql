import graphene

from server.ingredients.schema import Queries, CategoryMutations


class Query(Queries, graphene.ObjectType):
    pass


class Mutation(CategoryMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)