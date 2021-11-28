--https://projecteuler.net/problem=1

-- If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
-- Find the sum of all the multiples of 3 or 5 below 1000.

start_time = os.clock()

function multiples(value)
    sum = 0
    for i=0,value do
        if i%3 == 0 then
            --print (i, end=' ')
            sum = sum + i
        elseif i%5 == 0 then
            --print (i, end=' ')
            sum = sum + i
        end
        
    end
    return sum
end



a = multiples(10)
b = multiples(1000)

print(a, b)

end_time = os.clock()
elapsed_time = (end_time - start_time)*1000000
print(string.format("%.4f us", elapsed_time))