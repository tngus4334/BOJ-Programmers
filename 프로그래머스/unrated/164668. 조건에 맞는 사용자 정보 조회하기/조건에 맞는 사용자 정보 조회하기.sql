-- 코드를 입력하세요
SELECT B.USER_ID, B.NICKNAME, SUM(PRICE) TOTAL_SALES
FROM USED_GOODS_BOARD A JOIN USED_GOODS_USER B ON A.WRITER_ID=B.USER_ID
WHERE A.STATUS = 'DONE'
GROUP BY A.WRITER_ID
HAVING TOTAL_SALES>=700000
ORDER BY 3