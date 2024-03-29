-- 코드를 입력하세요
SELECT USER_ID,NICKNAME, CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) 전체주소, CONCAT(LEFT(TLNO,3),'-',SUBSTRING(TLNO,4,4),'-',RIGHT(TLNO,4)) 전화번호
FROM USED_GOODS_BOARD A JOIN USED_GOODS_USER B ON A.WRITER_ID=B.USER_ID
GROUP BY A.WRITER_ID
HAVING COUNT(*)>=3
ORDER BY 1 DESC