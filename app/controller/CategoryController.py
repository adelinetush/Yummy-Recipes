from app.models.model.Model import Category
#from app.models.model import Category
from app.models import db



class CategoryController:
    """Manage Category Controller"""
    def __init__(self):
        self.count = 1


    def add_category(self, cat):
        """Store Category to Database"""
        self.categories = [];
        if not db.session.query(Category).filter(Category.name == cat['name']).count():
            c = Category(cat['email'],cat['name'],cat['description'])
            db.session.add(c)
            db.session.commit()
        for cat in Category.query.filter(Category.email == cat['email']):
            self.categories.append(cat.serialize())
        return self.categories
        
    def get_user_category(self,email):
        guc = []
        for cat in Category.query.filter(Category.email == email):
            guc.append(cat.serialize())
        return guc

    def get_all_category(self):
        gac = []
        for cat in Category.query:
            gac.append(cat.serialize())
        return gac
        
    def delete_category(self, id):
        if(Category.query.filter(Category.id == id).count()>0):
            for cat in Category.query.filter(Category.id == id):
                db.session.delete(cat)
                db.session.commit()
            return True
        return False;

    def add_category_memory(self, cat):
        """Deprecated Store to Memory Functions"""
        c = None
        #c = Category(self.count, cat['email'],cat['name'],cat['description'])
        self.count += 1
        self.categories.append(c.serialize())
        return self.categories

    def delete_category_memory(self,item):
        """Deprecated Store to Memory Functions"""
        self.categories.remove(item)
        return True