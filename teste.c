library ieee; 
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity Maquina_de_doces is 
port (
    clk: in std_logic;
    reset: in std_logic;
    Ed, D1, D2, D3, D4: in std_logic;
    T, Ej, Eh, Ec, Eb: out std_logic
);
end Maquina_de_doces; 

architecture arch of Maquina_de_doces is 
    type stateType is (A0, A2, A4);
    signal state_reg, state_next : stateType; 
begin  
    process(clk, reset)
    begin
        if reset = '1' then
            state_reg <= A0;
        elsif (clk) then
            state_reg <= state_next;
        end if;
    end process; 

    process(Ed, D1, D2, D3, D4, state_reg) 
    begin 
        state_next <= state_reg;
        T <= '0';
        Ej <= '0';
        Eh <= '0';
        Ec <= '0';
        Eb <= '0';
        case state_reg is
            when A0 =>
                if (Ed = '1') then
                    T <= '0';
                    Ej <= '0';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '0';
                    state_next <= A2; 
                else
                    T <= '0';
                    Ej <= '0';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '0';
                    state_next <= A0; 
                end if;
            when A2 =>
                if (Ed = '1') then
                    T <= '0';
                    Ej <= '0';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '0';
                    state_next <= A4; 
                elsif (D1 = '1' and D2 ='0' and D3 = '0' and D4 = '0') then
                    T <= '0';
                    Ej <= '1';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '0';
                    state_next <= A0; 
                elsif (D1 = '0' and D2 ='1' and D3 = '0' and D4 = '0') then
                    T <= '0';
                    Ej <= '0';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '0';
                    state_next <= A2;  
                elsif (D1 = '0' and D2 ='0' and D3 = '1' and D4 = '0') then
                    T <= '0';
                    Ej <= '0';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '0';
                    state_next <= A2; 
                elsif (D1 = '0' and D2 ='0' and D3 = '0' and D4 = '1') then
                    T <= '0';
                    Ej <= '0';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '1';
                    state_next <= A0;
                else
                    T <= '0';
                    Ej <= '0';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '0';
                    state_next <= A2; 
                end if;
            when A4 =>
                if (Ed = '1') then
                    T <= '1';
                    Ej <= '0';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '0';
                    state_next <= A0; 
                elsif (D1 = '1' and D2 ='0' and D3 = '0' and D4 = '0') then
                    T <= '0';
                    Ej <= '1';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '0';
                    state_next <= A2; 
                elsif (D1 = '0' and D2 ='1' and D3 = '0' and D4 = '0') then
                    T <= '0';
                    Ej <= '0';
                    Eh <= '1';
                    Ec <= '0';
                    Eb <= '0';
                    state_next <= A0;  
                elsif (D1 = '0' and D2 ='0' and D3 = '1' and D4 = '0') then
                    T <= '0';
                    Ej <= '0';
                    Eh <= '0';
                    Ec <= '1';
                    Eb <= '0';
                    state_next <= A0; 
                elsif (D1 = '0' and D2 ='0' and D3 = '0' and D4 = '1') then
                    T <= '0';
                    Ej <= '0';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '1';
                    state_next <= A2;
                else
                    T <= '0';
                    Ej <= '0';
                    Eh <= '0';
                    Ec <= '0';
                    Eb <= '0';
                    state_next <= A4; 
                end if;
            when others =>
                T <= '0';
                Ej <= '0';
                Eh <= '0';
                Ec <= '0';
                Eb <= '0';
                state_next <= A0; 
        end case;
    end process;  
end architecture;
