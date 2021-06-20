import cx_Oracle as oracle
orcl_dsn = oracle.makedsn(host='localhost', port=1521, sid='xe') #192.168.2.131
conn = oracle.connect(dsn = orcl_dsn, user='jyhoon94', password='123456')


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
        sql = """insert into workout_diary 
            (workout_user, 
            workout_date, 
            workout_big, 
            workout_middle, 
            workout_small, 
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
    
    def getData(self, user_id):
        cursor = conn.cursor()
        sql = """select sum(workout_weight * WORKOUT_REPNUM) as volume, workout_date, workout_big as category
                from workout_diary
                where workout_user =: user_id
                group by workout_date, workout_big
                order by workout_date """
        cursor.execute(sql,(user_id))
        result = cursor.fetchall()
        return result
        