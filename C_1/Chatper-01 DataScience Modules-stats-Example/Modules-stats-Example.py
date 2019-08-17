import statistics as s

sales = [111,222,444,222,444,222,444,222,4455,222]

#
print(s.mean(sales)) #avg
print(max(sales)) #return max
print(min(sales)) #return min
print(sum(sales)) #return total 
print(len(sales)) #return count of items 

##
print(s.median(sales)) #return mid value  (if even count : sum or mid 2 val/2)
print(s.median_high(sales))
print(s.median_low(sales))


print(s.variance(sales)) #return var

print(s.stdev(sales)) #return sqrt() for var

print(s.median_high(sales))

print(s.mode(sales)) #return value which has highest freq/count

'''
stats function:
     count/len
     min
     max
     sum
     mean/avv
     mode
     median
     var
     stdev
     range                 : max - min  
     quantile              : min(firt value), 25% , 50%, 75% , max/100%
     percentile            : return given % value  
'''     
##range
print(max(sales) - min(sales))
print(min(sales), '- ', max(sales) )



##quantile
sales.sort() #sort the list
print(sales)

i = int(len(sales)/4)  #2
print(sales[0],sales[i],sales[i*2], sales[i*3] , sales[-1])  #-1 last value

#percentile
print(sales[3],sales[6])







