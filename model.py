import cx_Oracle as oracle
orcl_dsn = oracle.makedsn(host='localhost', port=1521, sid='xe') #192.168.2.131
conn = oracle.connect(dsn = orcl_dsn, user='jyh', password='123456')


class Record:
    # def __init__(self, date, big, middle, small, setNum, weight, repNum, etc):
    #     self.date = date
    #     self.big = big
    #     self.middle = middle
    #     self.small = small
    #     self.setNum = setNum
    #     self.weight = weight
    #     self.repNum = repNum
    #     self.etc = etc


    def checkId(self, user_id):
        cursor = conn.cursor()
        sql = """
            select user_id from user_info where user_id=:user_id
            """
        cursor.execute(sql, {"user_id":user_id})
        result = cursor.fetchone()
        return result

    def checkPw(self, user_id):
        cursor = conn.cursor()
        sql = """
            select user_pw from user_info where user_id=:user_id
        """
        cursor.execute(sql, {"user_id":user_id})
        result = cursor.fetchone()
        return result
    def save(self, user_id, date, big, middle, small, setNum, weight, repNum, etc):
        cursor = conn.cursor()
        sql = """insert into workout_db 
            (user_id, 
            workout_date, 
            workout_cat1, 
            workout_cat2, 
            workout_cat3, 
            workout_setNum, 
            workout_weight, 
            workout_repNum, 
            workout_etc) 
        values(:workout_user, :workout_date, :workout_big, :workout_middle, :workout_small, 
        :workout_setNum, :workout_weight, :workout_repNum, :workout_etc)
        """
        cursor.execute(sql,(user_id, date, big, middle, small, setNum, weight, repNum, etc))
        conn.commit()

    def login(self, user_id, user_pw):
        cursor = conn.cursor()
        sql = "select user_id, user_pw from user_info where user_id=:user_id and user_pw=:user_pw"
        cursor.execute(sql, {"user_id":user_id, "user_pw": user_pw})
        result = cursor.fetchone()
        return result
    
    def getAll(self, user_id):
        cursor = conn.cursor()
        sql="""
            select to_char(workout_date) as dates, workout_cat1, sum(workout_repNum * workout_weight) as volume
            from workout_db
            where user_id=:user_id
            group by workout_cat1, workout_date
            order by workout_date
        """
        cursor.execute(sql,{'user_id':user_id})
        result = cursor.fetchall()
        return result

    def getCategory(self, user_id, workout_cat1):
        cursor = conn.cursor()
        sql = """
        select to_char(workout_date) as dates,workout_cat1, sum(workout_repNum * workout_weight) as volume
        from workout_db
        where user_id=:user_id and workout_cat1 =:workout_cat1
        group by workout_cat1, workout_date
        order by workout_date
        """
        cursor.execute(sql,{"user_id":user_id, "workout_cat1": workout_cat1})
        result = cursor.fetchall()
        return result
        
        