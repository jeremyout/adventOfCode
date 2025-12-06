/* --- Part Two ---

You're sure that's the right password, but the door won't open. You knock, but nobody answers. You build a snowman while you think.

As you're rolling the snowballs for your snowman, you find another security document that must have fallen into the snow:

"Due to newer security protocols, please use password method 0x434C49434B until further notice."

You remember from the training seminar that "method 0x434C49434B" means you're actually supposed to count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.

Following the same rotations as in the above example, the dial points at zero a few extra times during its rotations:

    The dial starts by pointing at 50.
    The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
    The dial is rotated L30 to point at 52.
    The dial is rotated R48 to point at 0.
    The dial is rotated L5 to point at 95.
    The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
    The dial is rotated L55 to point at 0.
    The dial is rotated L1 to point at 99.
    The dial is rotated L99 to point at 0.
    The dial is rotated R14 to point at 14.
    The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.

In this example, the dial points at 0 three times at the end of a rotation, plus three more times during a rotation. So, in this example, the new password would be 6.

Be careful: if the dial were pointing at 50, a single rotation like R1000 would cause the dial to point at 0 ten times before returning back to 50!

Using password method 0x434C49434B, what is the password to open the door?

*/


using System.IO;

string filePath = "../day1input.txt"; 
try
{
    string[] fileContents = File.ReadAllLines(filePath);
    Console.WriteLine($"Total lines read: {fileContents.Length}");

    int totalZeros = 0;
    int dialPosition = 50;

    for (int i = 0; i < fileContents.Length; i++)
    {
        bool startsWithL = fileContents[i].StartsWith('L');
        bool startsWithR = fileContents[i].StartsWith('R');

        if (!startsWithL && !startsWithR)
        {
            throw new Exception("Line doesn't start with L or R");
        }
        // Check line to make sure it starts with only 1 
        if (!int.TryParse(fileContents[i].Substring(1), out int result))
        {
            throw new Exception($"The substring '{fileContents[i].Substring(1)}' cannot be parsed as an integer.");
        }

        while (result >= 100)
        {
            result -= 100;
        }

        if (startsWithL)
        {
            Console.WriteLine($"Subtracting {result} from current dial position");
            if (result > dialPosition)
            {
                Console.WriteLine("Will roll past 0, calculating delta");
                int delta = Math.Abs(dialPosition-result);
                Console.WriteLine($"Delta calculated to be {delta}");
                dialPosition = 100 - delta;
            } 
            else
            {
                dialPosition -= result;
            }
        } 
        else if (startsWithR)
        {
            Console.WriteLine($"Adding {result} to current dial position");
            if (dialPosition + result > 99)
            {
                Console.WriteLine("Will roll past 99, calculating delta");
                int delta = result + dialPosition - 100;
                Console.WriteLine($"Delta calculated to be {delta}");
                dialPosition = delta;
            }
            else
            {
                dialPosition += result;
            }
        }

        Console.WriteLine($"Dial position is now at {dialPosition}");

        if (dialPosition == 0)
        {
            totalZeros++;
        }
    }
    Console.WriteLine($"Dial position landed on zero {totalZeros} times");
}
catch (IOException e)
{
    Console.WriteLine($"Error reading file: {e.Message}");
}