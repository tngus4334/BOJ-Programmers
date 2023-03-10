-- 코드를 입력하세요
SELECT CATEGORY, SUM(SALES) AS TOTAL_SALES
FROM BOOK_SALES BS JOIN BOOK B ON BS.BOOK_ID = B.BOOK_ID
WHERE SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY CATEGORY
ORDER BY 1