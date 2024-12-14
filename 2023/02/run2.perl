#!/usr/bin/perl -l

my %bag = (
    qw/red/ => 12,
    qw/green/ => 13,
    qw/blue/ => 14,
    );
my $key = join("|", keys %bag);

my $sum = 0;
while (my $line = <>) {
    chomp;
    $line =~ s/Game ([0-9]*)://;
    my $game = $1;
    # print("\$game=$game");
    my %minbag = ();
    while ($line =~ /([^;]+);?/g) {
	my $draws = $1;
	# print("\$draws=$draws");
	while ($draws =~ /([0-9]+) ($key)/g) {
	    $count = $1;
	    $color = $2;
	    if (!exists($minbag{$color}) || $minbag{$color} < $count) {
		$minbag{$color} = $count;
	    }
	    # print("\$count=$count \$color=$color");
	}
    }
    my $prod = 1;
    foreach my $count (values %minbag) {
	$prod *= $count;
    }
    $sum += $prod;
}
print($sum);
