using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Task5Amazing
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void guna2Button1_Click(object sender, EventArgs e)
        {
            string slswdaw = "NAITCTF{Br3ak_P0int_G00d!}";
            if (sdapwdlsdx.Text == slswdaw)
            {
                MessageBox.Show("Flag correct!");
            }    
            else
            {
                MessageBox.Show("Flag Incorrect! Try again.");
            }
        }
    }
}
