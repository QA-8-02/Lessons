/****** Script for SelectTopNRows command from SSMS  ******/
SELECT ProductID
      ,[UnitPrice]
      ,[Quantity]
      ,[Discount]
	  , Quantity*UnitPrice*(1-Discount) as "���� ���� ����"
  FROM [Order Details]
  where ProductID=72