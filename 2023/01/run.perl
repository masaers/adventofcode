#!/usr/bin/perl

my $sum = 0;
while (<>) {
    print;
    if (/^[^1-9]*([1-9]).*([1-9])[^1-9]*$/) {
	$sum += int("$1$2");
    } elsif (/^[^1-9]*([1-9])[^1-9]*$/) {
	$sum += int("$1$1");
    } else {
	print("ERROR!\n");
    }
}
print("$sum\n")
