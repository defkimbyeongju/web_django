-- SQL 문 작성 시 주의사항
-- 세미콜론(;) 기준으로 하나의 SQL문 판별

-- 새로운 테이블을 생성
-- id, 이름, 직업, 능력, 국적, 소속회사, 나이
-- 필드명, 타입, 제약조건 순으로 작성
-- NOT NULL : 이 필드는 NULL 값일 수 없다는 제약조건

CREATE TABLE superheroes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    이름 TEXT NOT NULL,
    직업 TEXT NOT NULL,
    능력 TEXT,
    국적 TEXT,
    소속회사 TEXT,
    나이 INTEGER
);

-- 테이블명 변경하기
ALTER TABLE superheroes
RENAME TO superhero;

-- 새로운 컬럼 추가
ALTER TABLE superhero
ADD COLUMN 가입날짜 DATE;

-- 임시 컬럼 추가
-- 임시 컬럼 -> 곧삭제 컬럼
-- 곧삭제 컬럼 삭제

ALTER TABLE superhero
add COLUMN 임시 TEXT;

ALTER TABLE superhero
RENAME COLUMN 임시 TO 곧삭제;


-- vscode sqlite 익스텐션의 문제 때문인지 실행이 되지 않지만, DROP COLUMN은 열 삭제임.
ALTER TABLE superhero
DROP COLUMN 곧삭제;

-- 테이블 지우기
-- DROP TABLE superhero;

-- 스키마 확인
PRAGMA table_info('superhero');

