def print_binary_square(n):

    for i in range(1, n+1):
        if i%2==0:
            for j in range(1,n+1):
                if j%2==0:
                    print('0',end=' ')
                else:
                    print('1',end=' ')
            print()
        else:
            for j in range(1,n+1):
                if j%2==0:
                    print('1',end=' ')
                else:
                    print('0',end=' ')
            print()

#python
def data_masukk():
        import re

        masukan = input("masukkan data yang dipisahkan oleh koma\n")

        data = re.split(r',|;',masukan)

        email = re.findall(r'[\w\.-]+@[\w\.-]+',masukan)

        print(data)
        print(email)
data_masukk()

'''
SQL on how to join, create, and insert table

-- SQL

-- create a video table
CREATE TABLE video(
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  title TEXT NOT NULL,
  description TEXT,
  video_url TEXT NOT NULL,
  created_at datetime default current_timestamp,
  published_at default current_timestamp,
  PRIMARY KEY(id)
);

-- create a subtitle table
CREATE TABLE subtitle(
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  video_id INTEGER NOT NULL,
  srt_url TEXT,
  languages varchar NOT NULL,
  PRIMARY KEY(id)
);

-- insert some values
INSERT INTO subtitle(video_id,srt_url,languages) values ('01','subscene.com','indonesia')
,('02','subscene.com','indonesia');
INSERT INTO video(title,description,video_url) VALUES ('Save Private Ryan', 'film tentara','a.com')
,('ratatouille', 'tikus masak','english');

-- get film where the language is indonesia
SELECT video.title, subtitle.languages FROM video INNER join subtitle ON video.id = subtitle.id;
'''