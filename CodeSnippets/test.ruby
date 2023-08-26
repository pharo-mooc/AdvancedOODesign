#This file contains some tests showing the handling of private methods in ruby.
#

class C
	def zork(arg) ; return arg.x ; end 
	def fooSendingSelfX ; self.x end
	def fooAccessingX; x; end
	private
	def x; return 1; end
end
class D < C
	public
	def x; return 2; end
end

#C.new.foo
#=> failed test.ruby:3:in `foo': private method `x' called for #<C:0x007ffef4962fd0> (NoMethodError)

puts "C.new.fooSendingSelfX" 
puts "failed"
# prints "failed"

puts "C.new.fooAccessingX"
puts C.new.fooAccessingX 
# 1

puts "D.new.fooSendingSelfX"
puts D.new.fooSendingSelfX 
# 2

puts "D.new.fooAccessingX"
puts D.new.fooAccessingX 
# 2

puts "C.new.zork(C.new)"
puts "failed"
# prints "failed"

puts "C.new.zork(D.new)"
puts C.new.zork(D.new) 
#2