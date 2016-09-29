amount = 20000000
nums = {2,3}
index = 1
i = 1

socket = require('socket')

function start()
	start_time = socket.gettime()
end

function ellapsed()
	return socket.gettime() - start_time
end

start()

function isPrime(i,nums)
	root = math.sqrt(i)
	for v, num in pairs(nums) do
		if (i % num == 0) then
			return false
		elseif num >= root or num == nil then
			return true
		end
	end
end

for i = 3,amount,2 do
	prime = isPrime(i,nums)
	if prime  then
		nums[index + 1] = i
		index = index + 1
	end
end

print("Time (S):"..ellapsed())
io.read()

for index, num in pairs(nums) do
	print(num)
end
io.read()

change = {}
for index,num in pairs(nums) do
	if index ~= 1 then
		change[index] = nums[index] - nums[index - 1]
	end
end

for index,num in pairs(change) do
	print(num)
end

io.read()
