use strict;
# Abandoned Python because this simple idea took forever to
# run. Surprising that Python should have such an inferior regex
# engine!

my $line = <>;
chomp $line;
my $re = "^(?:" . join("|", split(/, */, $line)) . ")+\$";
my $result = 0;
while (<>) {
    ++$result if /$re/;
}
print("$result\n")
