row_data = File.open(File.join(__dir__, 'data.txt'), 'r').readlines
row_data = row_data.map(&:to_i).sort

def two_sum(sum_result, data)
  data.each_with_index do |num, index|
    next if num.nil?

    # puts "#{index}: #{num}"
    find_num = sum_result - num
    temp_ary = data[(index+1)...data.length]

    return [num, find_num] if temp_ary.include? find_num
  end
end

def three_sum(sum_result, data)
  data.each_with_index do |num, index|
    next if num.nil?

    find_num = sum_result - num
    temp_ary = data[(index + 1)...data.length]

    sub_result = two_sum(find_num, temp_ary)

    next if sub_result.empty?

    return sub_result << num
  end
end

result = three_sum(2020, row_data)

puts result.to_s
puts result.inject(:*)

## TODO: Try to use map
