
--This should pass
context con1 is

END context con1;

--These should fail
context con1 is
end context con1;

context co1 is

eNd context con1;
