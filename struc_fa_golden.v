module struc_fa_golden(
	input A, B, Cin, clk, en,
	output sum, Cout
    );
	wire w1, w2, w3, da, db, dCin, dsum, dCout;

	xor g1 (w1, da, db);
	xor g3 (dsum, w1, dCin);
	and g4 (w2, w1, dCin);
	and g5 (w3, da, db);
	or  g6 (dCout, w2, w3);

	
	dff a1 (da, A, clk);
	dff a2 (db, B, clk);
	dff a3 (dCin, Cin, clk);
	dff a4 (sum, dsum, clk);
	dff a5 (Cout, dCout, clk);
	
endmodule

module dff(q, d, clk);
	input  d, clk;
	output reg q;

always @ (posedge clk)
	q = d;
endmodule


`timescale 1ns/ 1ps

module Testbench_adder();
 reg A, B, Cin, en, clk;
 wire sum, Cout;  

 //instantiation
 struc_fa_golden dut(
    .A(A),
    .B(B),
	.en(en),
    .Cin(Cin),
	.clk(clk),
    .sum(sum),
    .Cout(Cout)
   );
    initial begin

	 $monitor(" %b, %b, %b, %b, %b, %b",A, B, Cin, en, sum , Cout);
	 
	 //$dumpfile ("struc_fa_golden-out.vcd"); 
	 //$dumpvars(0, Testbench_adder);
	 clk = 0; A = clk; B = clk; Cin = clk; en = 0;
	end

	always @ (negedge clk) 
	begin
		#12 en = 1;
		#1  en = 0;
      end

		always 
			#1 clk = ~clk;
		always 
			#3 A = ~A;
		always 
			#2 B = ~B;
		always 
			#4 Cin = ~Cin;
//-----------------------------------------------------------
	
	initial #100 $finish;
endmodule 
