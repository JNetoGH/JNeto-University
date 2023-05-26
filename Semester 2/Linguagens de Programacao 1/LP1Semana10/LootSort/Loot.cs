using System;

namespace LootSort
{
    /// <summary>
    /// The Loot class should implement IComparable<Loot>
    /// and override GetHashCode() and Equals()
    /// </summary>
    public class Loot: IComparable<Loot>
    {
        /// <summary>Type of loot.</summary>
        public LootType Kind { get; }

        /// <summary>Loot description.</summary>
        public string Description { get; }

        /// <summary>Loot value.</summary>
        public float Value { get; }

        /// <summary>
        /// Create a new instance of loot.
        /// </summary>
        /// <param name="kind">Type of loot.</param>
        /// <param name="description">Loot description.</param>
        /// <param name="value">Loot value.</param>
        public Loot(LootType kind, string description, float value)
        {
            Kind = kind;
            Description = description;
            Value = value;
        }

        public int CompareTo(Loot other)
        {
            // name
            if (!Kind.ToString().Equals(other.Kind.ToString()))
                return String.Compare(Kind.ToString(), other.Kind.ToString(), StringComparison.Ordinal);

            // value
            if (Value != other.Value)
                return Value > other.Value ? -1 : 1;
            
            // description
            return String.Compare(Description, other.Description, StringComparison.Ordinal);
        }

        public override int GetHashCode()
        {
            return Kind.GetHashCode() ^ Value.GetHashCode() ^ Description.GetHashCode();
        }

        public override bool Equals(object obj)
        {
            if (obj == null || GetType() != obj.GetType())
                return false;
            Loot otherPlayer = (Loot)obj;
            return Kind == otherPlayer.Kind && Value == otherPlayer.Value && Description == otherPlayer.Description;
        }
        
        /// <summary>
        /// Return a nicely formatted string representing the loot instance.
        /// </summary>
        /// <returns>
        /// A nicely formatted string representing the loot instance.
        /// </returns>
        public override string ToString() =>
            $"[{Kind,15}]\t{Value:f2}\t{Description}";
    }
}