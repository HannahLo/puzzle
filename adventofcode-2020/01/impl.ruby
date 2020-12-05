SUM_RESULT = 2020.freeze

data = File.open(File.join(__dir__, 'data.txt'), 'r').readlines

data.map!(&:to_i)

result = []
data.each_with_index do |num, index|
  next if num.nil?

  # puts "#{index}: #{num}"
  find_num = SUM_RESULT - num

  if data.include? find_num
    result = [num, find_num]
  end
end

puts result.to_s
puts result.inject(:*)
