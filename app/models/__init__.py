from app import db, logger

select = db.select
execute = db.session.execute

class MyBaseClass:
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception:
            db.session.rollback()
            raise

    @classmethod
    def get_all(cls):
        return execute(select(cls)).scalars().all()
        
    @classmethod
    def commit(self):
        db.session.commit()

    @classmethod
    def get(cls, id):
        try:
            return db.session.get(cls, id)
        except Exception:
            db.session.rollback()
            raise

    def as_dict_name(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    

    # TIPS: Возможная оптимизация кода!
    # [ ]: Вместо того, чтобы каждый раз открывать поток файла, 
    #      можно создать метод, который получает на вход список этих объектов
    #      и сохраняет их разом
    # [ ]: Сравнить показатели такого подхода с существующим
    def save_to_file(self, filename):
        attr = self.as_dict_name()
        try:
            with open(filename, 'a', encoding='UTF8') as f:
                f.write(",".join(map(str, attr.values()))+"\n")
        except:
            with open(filename, 'w+', encoding='UTF8') as f:
                f.write(",".join(map(str, attr.values())))
    
        
        